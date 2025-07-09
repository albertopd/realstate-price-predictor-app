import re
from urllib.parse import urljoin

import requests
import streamlit as st

from enums import (
    PropertyType,
    ApartmentSubtype,
    HouseSubtype,
    CommonSubtype,
    Province,
    EPCScore,
)

API_BASE_URL = "https://challenge-api-deployment-13tu.onrender.com"
API_PREDICT_ENDPOINT = "/predict"

# --- Helpers ---

# Combine subtype enums based on selected type ---
def get_subtype_options(property_type: PropertyType):
    common = [e.value for e in CommonSubtype]
    if property_type == PropertyType.APARTMENT:
        specific = [e.value for e in ApartmentSubtype]
    elif property_type == PropertyType.HOUSE:
        specific = [e.value for e in HouseSubtype]
    else:
        specific = []
    return [""] + common + specific  # "" = no selection


# --- UI ---

st.title("🏠 Real Estate Price Predictor")
st.markdown("*Powered by ML API hosted on render.com*")

st.subheader("Property Details:")

habitable_surface = st.slider(
    "Habitable Surface (m²)", min_value=10, max_value=1000, value=10, step=1
)

# Property type dropdown
property_type = st.selectbox(
    label="Property Type",
    options=[e.value for e in PropertyType],
    format_func=lambda x: x.replace("_", " ").title(),
)

# Property subtype dropdown (dependent)
subtype_options = get_subtype_options(PropertyType(property_type))
property_subtype = st.selectbox(
    "Subtype", subtype_options, format_func=lambda x: x.replace("_", " ").title()
)

postcode = st.number_input("Postcode", min_value=1000, max_value=9999, step=1)

# EPC dropdown
epc_score = st.selectbox(
    "EPC Score",
    options=[""] + [e.value for e in EPCScore],
    format_func=lambda x: x if x else " ",
)

terrace_surface = st.slider(
    "Terrace Surface (m²)", min_value=0, max_value=500, value=0, step=1
)
garden_surface = st.slider(
    "Garden Surface (m²)", min_value=0, max_value=2000, value=0, step=1
)

bedrooms = st.slider("Bedrooms", min_value=0, max_value=10, value=0, step=1)
bathrooms = st.slider("Bathrooms", min_value=0, max_value=10, value=0, step=1)
toilets = st.slider("Toilets", min_value=0, max_value=10, value=0, step=1)

st.markdown("### Features:")
features = {
    "hasAirConditioning": st.checkbox("Air Conditioning"),
    "hasArmoredDoor": st.checkbox("Armored Door"),
    "hasAttic": st.checkbox("Attic"),
    "hasBasement": st.checkbox("Basement"),
    "hasDiningRoom": st.checkbox("Dining Room"),
    "hasDressingRoom": st.checkbox("Dressing Room"),
    "hasFireplace": st.checkbox("Fireplace"),
    "hasGarden": st.checkbox("Garden"),
    "hasHeatPump": st.checkbox("Heat Pump"),
    "hasLift": st.checkbox("Lift"),
    "hasLivingRoom": st.checkbox("Living Room"),
    "hasOffice": st.checkbox("Office"),
    "hasPhotovoltaicPanels": st.checkbox("Photovoltaic Panels"),
    "hasSwimmingPool": st.checkbox("Swimming Pool"),
    "hasTerrace": st.checkbox("Terrace"),
    "hasVisiophone": st.checkbox("Visiophone"),
}

st.markdown("---")

if st.button("Predict Price"):
    input_data = {
        "type": property_type,
        "habitableSurface": habitable_surface,
        **features,
    }

    # Optional fields only if set
    if postcode:
        input_data["postCode"] = int(postcode)
    if property_subtype:
        input_data["subtype"] = property_subtype
    if epc_score:
        input_data["epcScore"] = epc_score
    if terrace_surface > 0:
        input_data["terraceSurface"] = terrace_surface
    if garden_surface > 0:
        input_data["gardenSurface"] = garden_surface
    if bedrooms > 0:
        input_data["bedroomCount"] = bedrooms
    if bathrooms > 0:
        input_data["bathroomCount"] = bathrooms
    if toilets > 0:
        input_data["toiletCount"] = toilets

    payload = {"data": input_data}
    url = urljoin(API_BASE_URL, API_PREDICT_ENDPOINT)

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            prediction = response.json()["data"]["prediction"]
            st.markdown("<br>", unsafe_allow_html=True)
            st.success(f"💰 Predicted Property Price: €{prediction:,.2f}")
        elif response.status_code == 422:
            json_response = response.json()
            msg = json_response["detail"][0]["msg"]
            st.markdown("<br>", unsafe_allow_html=True)
            st.error(f"⚠️ {msg}")
        elif response.status_code == 500:
            json_response = response.json()
            error = json_response["error"]
            st.markdown("<br>", unsafe_allow_html=True)
            st.error(f"⛔ {error}")
    except Exception as e:
        st.markdown("<br>", unsafe_allow_html=True)
        st.error(f"⛔ Request failed: {str(e)}")

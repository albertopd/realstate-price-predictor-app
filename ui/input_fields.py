import streamlit as st
from enums import PropertyType, EPCScore
from logic.helpers import get_subtype_options, add_space_before_caps

def collect_property_inputs():
    data = {}
    data["habitableSurface"] = st.slider("Habitable Surface (m²) 🔹", 10, 1000, 10)
    data["postCode"] = st.number_input("Postal Code 🔹", 1000, 9999, step=1)

    property_type = st.selectbox(
        "Property Type 🔹",
        [e.value for e in PropertyType],
        format_func=lambda x: x.replace("_", " ").title(),
    )
    data["type"] = property_type

    subtype_options = get_subtype_options(PropertyType(property_type))
    subtype = st.selectbox("Property Subtype", subtype_options, format_func=lambda x: x.replace("_", " ").title())
    if subtype:
        data["subtype"] = subtype

    epc = st.selectbox("EPC Score", [""] + [e.value for e in EPCScore])
    if epc:
        data["epcScore"] = epc

    if (ts := st.slider("Terrace Surface (m²)", 0, 500)) > 0:
        data["terraceSurface"] = ts
    if (gs := st.slider("Garden Surface (m²)", 0, 2000)) > 0:
        data["gardenSurface"] = gs
    if (b := st.slider("Bedrooms", 0, 10)) > 0:
        data["bedroomCount"] = b
    if (ba := st.slider("Bathrooms", 0, 10)) > 0:
        data["bathroomCount"] = ba
    if (t := st.slider("Toilets", 0, 10)) > 0:
        data["toiletCount"] = t

    st.markdown("#### Features:")
    features = [
        "hasAirConditioning", "hasArmoredDoor", "hasAttic", "hasBasement",
        "hasDiningRoom", "hasDressingRoom", "hasFireplace", "hasGarden",
        "hasHeatPump", "hasLift", "hasLivingRoom", "hasOffice",
        "hasPhotovoltaicPanels", "hasSwimmingPool", "hasTerrace", "hasVisiophone"
    ]
    for f in features:
        data[f] = st.checkbox(add_space_before_caps(f.replace("has", "")), key=f)

    return data

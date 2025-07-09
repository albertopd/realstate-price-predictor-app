import streamlit as st
from logic.api_client import predict_price

def handle_prediction(input_data):
    payload = {"data": input_data}
    try:
        response = predict_price(payload)

        st.markdown("<br>", unsafe_allow_html=True)

        if response.status_code == 200:
            prediction = response.json()["data"]["prediction"]
            st.success(f"💰 Predicted Property Price: €{prediction:,.2f}")

        elif response.status_code == 422:
            msg = response.json()["detail"][0]["msg"]
            st.error(f"⚠️ {msg}")

        elif response.status_code == 500:
            error = response.json()["error"]
            st.error(f"⛔ {error}")

        else:
            st.error(f"⛔ API Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"⛔ Request failed: {str(e)}")

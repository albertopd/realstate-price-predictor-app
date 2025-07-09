import streamlit as st
from ui.header import render_header
from ui.input_fields import collect_property_inputs
from ui.buttons import handle_prediction

st.set_page_config(page_title="Real Estate Predictor", layout="centered")

render_header()
input_data = collect_property_inputs()

st.markdown("---")

if st.button("Predict Price"):
    handle_prediction(input_data)

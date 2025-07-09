import streamlit as st
from ui.header import render_header
from ui.input_fields import collect_property_inputs
from ui.buttons import handle_prediction

st.set_page_config(page_title="Real Estate Predictor", layout="wide")

# Center content using empty columns on left and right
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    render_header()

    input_data = collect_property_inputs()

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Predict Price", type="primary"):
        handle_prediction(input_data)

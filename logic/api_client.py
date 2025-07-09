import requests
from urllib.parse import urljoin
import streamlit as st

def predict_price(payload):
    url = urljoin(
        st.secrets["predict_api"]["base_url"],
        st.secrets["predict_api"]["predict_endpoint"],
    )
    return requests.post(url, json=payload)

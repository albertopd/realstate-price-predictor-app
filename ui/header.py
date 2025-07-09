import streamlit as st

def render_header():
    st.title("🏠 Real Estate Price Predictor")
    st.markdown("*Powered by ML API hosted on render.com*")
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h3 style="margin: 0;">Property Details:</h3>
            <p style="font-size:12px; color:gray; margin: 0;">
                <em>Fields marked with🔹</span> are <strong>mandatory</strong>.</em>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

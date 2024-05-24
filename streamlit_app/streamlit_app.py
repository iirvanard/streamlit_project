import streamlit as st
from utils.image import get_image_as_base64

st.set_page_config(layout="wide")

left_space, middle, right_space = st.columns([1, 2, 1])

with middle:
    _, mid, _ = st.columns(3)
    st.markdown(f"""
    <div style="display: flex; justify-content: center; flex-direction: column; align-items: center; text-align: center;">
        <img src="data:image/png;base64,{get_image_as_base64('./streamlit_app/static/logo.png')}" alt="Logo" style="max-width: 100%;">
        <p style=" margin-bottom: 15%;">Train Wheels Defect App</p>
    </div>
""",
                unsafe_allow_html=True)

    col1, col2 = st.columns([4, 1])
    with col1:
        if st.button(label="sign in", type="primary"):
            st.switch_page("pages/login.py")
    with col2:
        if st.button(label="sign up", type="primary"):
            st.switch_page("pages/register.py")

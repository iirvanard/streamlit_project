import streamlit as st
from st_pages import hide_pages

hide_pages(["streamlit_app", "auth"])
st.switch_page("pages/home.py")

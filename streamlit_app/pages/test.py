import streamlit as st
from core.supabase import AuthClient
from st_pages import hide_pages

hide_pages(["streamlit_app", "auth"])

auth = AuthClient()

st.text("test")

import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state='collapsed')

if st.sidebar.button(label="Back", use_container_width=True):
    st.switch_page('pages/home.py')

st.header("test page")

st.image('streamlit_app/static/test.png', use_column_width=True)

import streamlit as st
from utils.modal import Modal
from st_pages import hide_pages

hide_pages(["streamlit_app", "auth"])
modal = Modal(
    "Demo Modal",
    key="demo-modal",

    # Optional
    padding=20,  # default value
    max_width=744  # default value
)


def submit():
    st.rerun()


open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        email = st.text_input("Email")
        password = st.text_input("password")
        example = st.text_input("example")
        if st.button("Submit", type="primary"):
            st.success("test")

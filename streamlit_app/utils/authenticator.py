import streamlit as st


class authenticators:

    def login(self, token):
        st.session_state["token"] = token
        st.session_state["logged_in"] = True

    def logout(self):
        st.session_state.clear()

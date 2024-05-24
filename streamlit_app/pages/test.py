import streamlit as st

<<<<<<< HEAD
st.set_page_config(layout="wide", initial_sidebar_state='collapsed')

if st.sidebar.button(label="Back", use_container_width=True):
    st.switch_page('pages/home.py')

st.header("test page")

st.image('streamlit_app/static/test.png', use_column_width=True)
=======

@st.experimental_dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()


if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d

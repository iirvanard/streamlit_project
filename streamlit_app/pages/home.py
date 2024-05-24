import streamlit as st
from utils.image import get_image_as_base64

st.set_page_config(layout="wide", initial_sidebar_state='collapsed')

background_image = get_image_as_base64("./streamlit_app/static/background.png")
page_style = f"""
<style>
[data-testid="stAppViewContainer"] {{
  background-image: url('data:image/png;base64,{background_image}');
  height: 100%; 
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}}

button[kind="secondary"] {{
  background-color: #252525;
}}

button[kind="secondary"] p {{
  color: #ffffff;
}}

[data-testid="column"]{{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}}


</style>
"""

st.html(body=page_style, )

page_element = """
<style>
.title {
    display: flex;
    flex-direction: column;
}

.title > div {
    color: white;
    font-weight: 800; 
    font-size: 70px;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("""
<div class="title">
    <div>SAFETY</div>
    <div>NO</div>
    <div>LIMIT</div>
</div>
""",
                unsafe_allow_html=True)

with col2:
    if st.button("Run Test >", use_container_width=True):
        st.switch_page("pages/test.py")
    if st.button("The Device we use >", use_container_width=True):
        st.switch_page("pages/page1.py")
    if st.button("Exit >", use_container_width=True):
        st.text("Run Test")

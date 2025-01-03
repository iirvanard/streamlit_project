import streamlit as st
from core.supabase.supabase_auth import SupabaseAuth
from utils.image import get_image_as_base64
from st_click_detector import click_detector
import time

st.set_page_config(
    layout="wide",
    page_icon="./streamlit_app/static/logo.png",
    page_title="login - SMAR+PARS",
)

auth = SupabaseAuth()

if 'logout' in st.session_state:
    st.toast("logout success")
    st.session_state.clear()

st.html(body="""
        <style>
            button[title='View fullscreen']{
                visibility: hidden;
            }
            h1 > div > a {
                display: none !important;
            }
            h2 > div > a {
                display: none !important;
            }
            h3 > div > a {
                display: none !important;
            }
            h4 > div > a {
                display: none !important;
            }
            h5 > div > a {
                display: none !important;
            }
            h6 > div > a {
                display: none !important;
            }
            .block-container {
                padding-top:0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
            .st-emotion-cache-1mjbses {
                flex-direction:column-reverse;
            }
            .st-emotion-cache-1mjbses {
                    flex-direction:column-reverse;
                }
            div[data-testid='stHorizontalBlock']{
                gap:0;
            }          
            div[data-testid='stVerticalBlock']:nth-of-type(1){
                gap:0;
            }   
            div[data-testid='column']:nth-of-type(2){
                margin-left: 1rem;
                margin-right: 1rem;
            }
            div[data-testid='column']:nth-of-type(1) img {
                border-top-right-radius: 20px;
                border-bottom-right-radius: 20px;
            }        
            div[data-testid='stCheckbox'] {
                margin-top: 20px;
                margin-bottom: 20px;
            }
        </style>
    """, )


def login():
    st.markdown(f"""
    <div style='text-align: center;'>
        <img src="data:image/png;base64,{get_image_as_base64("./streamlit_app/static/logo.png", )}" alt="Your image" />
        <h1>welcome back</h1>
        <p>sign in to access your account</p>
    </div>
    """,
                unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    st.markdown("""
    <style>
    div[data-testid="stCheckbox"] {
        margin-top: 15px;
        margin-bottom: 15px;
    }
    </style>
    """,
                unsafe_allow_html=True)

    if st.checkbox('remember me!'):
        st.write("test get user")
        st.text(auth.get_user())
    button = st.button("Login", type="primary", use_container_width=True)
    content = '''<div style="text-align:center;margin-bottom:5%;"><span>New Member? <a href='#' id="register" target="_self">Register now</a></span></div>'''
    clicked = click_detector(content)
    if clicked:
        st.switch_page('pages/register.py')

    if button:
        try:
            if email != "" and password != "":
                with st.spinner("loading..."):

                    auth.login_request(email, password)

                    seconds_to_wait = 3
                    while seconds_to_wait > 0:
                        time.sleep(1)
                        seconds_to_wait -= 1
                        st.toast("Redirecting in {} seconds...".format(
                            seconds_to_wait))

                    st.switch_page('pages/home.py')
            else:
                raise ValueError("Please enter both email and password.")
        except Exception as e:
            st.toast(str(e))


# Hide auth page if user is logged in
if auth.get_user():
    st.switch_page("pages/home.py")
else:
    left, right = st.columns([3, 1.5])
    with left:
        st.markdown(
            f"""<img src="data:image/png;base64,{get_image_as_base64("./streamlit_app/static/background.png", )}" style="width:100%;height:100%;object-fit:cover;" />""",
            unsafe_allow_html=True)

    with right:
        login()

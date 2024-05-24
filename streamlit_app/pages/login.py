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
<<<<<<< HEAD
            .st-emotion-cache-1mjbses {
                    flex-direction:column-reverse;
                }
=======
       
          
            .st-emotion-cache-1mjbses {
                    flex-direction:column-reverse;
                }
            
>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d
            div[data-testid='stHorizontalBlock']{
                gap:0;
            }          
            div[data-testid='stVerticalBlock']:nth-of-type(1){
                gap:0;
            }   
<<<<<<< HEAD
=======
            
>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d
            div[data-testid='column']:nth-of-type(2){
                margin-left: 1rem;
                margin-right: 1rem;
            }
<<<<<<< HEAD
=======

            
>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d
            div[data-testid='column']:nth-of-type(1) img {
                border-top-right-radius: 20px;
                border-bottom-right-radius: 20px;
            }        
<<<<<<< HEAD
=======

>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d
            div[data-testid='stCheckbox'] {
                margin-top: 20px;
                margin-bottom: 20px;
            }
<<<<<<< HEAD
        </style>
    """, )
=======
    

        </style>
    """, )
#  header[data-testid='stHeader'] {
#             display: none;
#         }
>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d


def login():
    st.markdown(f"""
    <div style='text-align: center;'>
        <img src="data:image/png;base64,{get_image_as_base64("./streamlit_app/static/logo.png", )}" alt="Your image" />
        <h1>welcome back</h1>
        <p>sign in to access your account</p>
    </div>
    """,
                unsafe_allow_html=True)

<<<<<<< HEAD
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
=======
    email = st.text_input("Email", value="t@t.com")
    password = st.text_input("Password", type="password", value="123123")
>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d
    st.markdown("""
    <style>
    div[data-testid="stCheckbox"] {
        margin-top: 15px;
        margin-bottom: 15px;
    }
    </style>
    """,
                unsafe_allow_html=True)

<<<<<<< HEAD
    if st.checkbox('remember me!'):
        st.write("test get user")
        st.text(auth.get_user())
    button = st.button("Login", type="primary", use_container_width=True)
    content = '''<div style="text-align:center;margin-bottom:5%;"><span>New Member? <a href='#' id="register" target="_self">Register now</a></span></div>'''
    clicked = click_detector(content)
    if clicked:
=======
    if (st.checkbox('remember me!')):
        st.write("test get user")
        st.text(auth.get_user())
    button = st.button("Login", type="primary", use_container_width=True)
    content = '''<div style="text-align:center;margin-bottom:5%;"><span>New Member? <a  href='#' id="register" target="_self">Register now</a></span></div>'''
    clicked = click_detector(content)
    if (clicked):
>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d
        st.switch_page('pages/register.py')

    if button:
        try:
            if email != "" and password != "":
<<<<<<< HEAD
                with st.spinner("loading..."):

                    auth.login_request(email, password)

                    seconds_to_wait = 3
                    while seconds_to_wait > 0:
                        time.sleep(1)
                        seconds_to_wait -= 1
                        st.toast("Redirecting in {} seconds...".format(
                            seconds_to_wait))

=======
                with st.spinner("Logging in..."):
                    auth.login_request(email, password)
                    # st.toast(
                    #     "Login successful. Redirecting to the next page in 3 seconds.",
                    #     icon=":material/check_circle:")
                    st.toast(
                        "Login successful. Redirecting to the next page in 3 seconds.",
                    )
                    time.sleep(3)
>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d
                    st.switch_page('pages/home.py')
            else:
                raise ValueError("Please enter both email and password.")
        except Exception as e:
<<<<<<< HEAD
=======

            # st.toast(str(e), icon=":material/error:")
>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d
            st.toast(str(e))


# Hide auth page if user is logged in
if auth.get_user():
    st.switch_page("pages/home.py")
else:
    left, right = st.columns([3, 1.5])
    with left:
<<<<<<< HEAD
        st.markdown(
            f"""<img src="data:image/png;base64,{get_image_as_base64("./streamlit_app/static/background.png", )}" style="width:100%;height:100%;object-fit:cover;" />""",
            unsafe_allow_html=True)
=======
        # st.image("./streamlit_app/static/background.png")
        st.markdown(f"""
        <img src="data:image/png;base64,{get_image_as_base64("./streamlit_app/static/background.png", )}" style="width:100%;height:100%;object-fit:cover;" />

    """,
                    unsafe_allow_html=True)
>>>>>>> 2450d732be8294214493ca8f73e2309f823bb56d

    with right:
        login()

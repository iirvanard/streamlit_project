import streamlit as st
from core.supabase.supabase_auth import SupabaseAuth
from utils.image import get_image_as_base64
from st_click_detector import click_detector
from streamlit_url_fragment import get_fragment

st.set_page_config(
    layout="wide",
    page_icon="./streamlit_app/static/logo.png",
    page_title="register - SMAR+PARS",
)

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

#    header[data-testid='stHeader'] {
#                 display: none;
#             }


# Register function
def register():
    current_value = get_fragment()
    if current_value is not None or current_value == '':
        if (current_value == '#terms'):
            st.write(current_value)
        if (current_value == '#Conditions'):
            st.write(current_value)

    st.markdown(f"""
    <div style='text-align: center;'>
        <img src="data:image/png;base64,{get_image_as_base64("./streamlit_app/static/logo.png", )}" alt="logo"  />
        <h1>Get Started</h1>
        <p>by creating a free account.</p>
    </div>
    """,
                unsafe_allow_html=True)

    fname = st.text_input("Full Name", placeholder="John Doe")
    email = st.text_input("Email", placeholder="example@email.com")
    phone_number = st.text_input("Phone Number", placeholder="+62 8.......")
    password = st.text_input("Password",
                             type="password",
                             placeholder="Strong Password")
    confirm_password = st.text_input("Confirm Password",
                                     type="password",
                                     placeholder="Confirm Strong Password")

    agreements = st.checkbox(
        'By checking the box you agree to our [Terms](#terms) and [Conditions](#Conditions).',
        key="my_checkbox",
    )
    button = st.button("Register", type="primary", use_container_width=True)
    content = '''<div style="text-align:center;margin-bottom:5%;"><span>New Member? <a href="#" id="login" target="_self">Already a member? </a></span></div>'''
    clicked = click_detector(content)
    if (clicked):
        st.switch_page('pages/login.py')
    if button:
        try:
            if password == confirm_password:
                if (not agreements):
                    raise ValueError("You must check terms and conditions")
                else:
                    with st.spinner("Registering..."):
                        auth.register_request(
                            fname=fname,
                            email=email,
                            password=password,
                            phone=phone_number,
                        )
                        # st.toast(
                        #     "Account created successfully. You can now log in.",
                        #     icon=":material/circle_check:")
                        st.toast(
                            "Account created successfully. You can now log in.",
                        )

            else:
                raise ValueError("Passwords do not match")
        except Exception as e:
            # st.toast(str(e), icon=":material/error:")
            st.toast(str(e))


auth = SupabaseAuth()

# Hide auth page if user is logged in
if auth.get_user():
    st.switch_page("pages/home.py")
else:
    left, right = st.columns([3, 1.5])
    with left:
        # st.image("./streamlit_app/static/background.png")
        st.markdown(f"""
        <img src="data:image/png;base64,{get_image_as_base64("./streamlit_app/static/background.png", )}" style="width:100%;height:100%;object-fit:cover;" />

    """,
                    unsafe_allow_html=True)

    with right:
        register()

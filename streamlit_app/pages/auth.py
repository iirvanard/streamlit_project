import streamlit as st
from st_pages import hide_pages
from core.supabase import AuthClient
from utils.authenticator import authenticators
import base64

hide_pages(["streamlit_app", "auth"])

auth = AuthClient()
auth_ = authenticators()


@st.cache_data
def get_image_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def login():
    st.markdown(f"""
    <div style='text-align: center;'>
        <img src="data:image/png;base64,{get_image_as_base64("assets/img/logo.png", )}" alt="Your image" />
        <h1>welcome back</h1>
        <p>sign in to access your account</p>
    </div>
    """,
                unsafe_allow_html=True)

    email = st.text_input("Email", value="imnot404@gmail.com")
    password = st.text_input("Password", type="password", value="Irvaners123@")

    test = st.checkbox('remember me!')

    if st.button("Login"):
        if email != "" and password != "":
            try:
                with st.spinner("Logging in..."):
                    response = auth.loginRequest(email, password)
                    if (response.status_code == 200):
                        data = response.json()
                        auth_.login(token=data['access_token'])
                        st.success("Login successful!")
                        st.switch_page("pages/home.py")
                    else:
                        raise ValueError("Check your email/password!!!")
                    # st.switch_page("home.py")

            except Exception as e:
                st.error(str(e))

        else:
            st.error("Please enter both email and password.")


# Register function
def register():
    st.markdown(f"""
    <div style='text-align: center;'>
        <img src="data:image/png;base64,{get_image_as_base64("assets/img/logo.png", )}" alt="Your image" />
        <h1>Get Started</h1>
        <p>by creating a free account.</p>
    </div>
    """,
                unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password == confirm_password:
            # Register user with Supabase
            try:
                with st.spinner("Registering..."):
                    response = auth.registerRequest(email, password)
                    if (response.status_code == 200):
                        st.success("Register successful!")
                        st.success("Now you can login!")
                    else:
                        raise ValueError(response.json())

            except Exception as e:
                st.error(str(e))
        else:
            st.error("Passwords do not match")


def forgot():
    st.text("forgot password")


logged_in = st.session_state.get('logged_in', False)

# Hide auth page if user is logged in
if logged_in:
    st.switch_page("pages/home.py")

option = st.sidebar.radio("Choose an option",
                          ("Register", "Login", "forgot password"))

# Display the appropriate page based on the selected option
if option == "Login":
    login()
elif option == "Register":
    register()
else:
    forgot()

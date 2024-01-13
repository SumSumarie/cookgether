import streamlit as st
from src.user_profile import user_profile_page

# REMOVE THIS CODE
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
###


def login_page():
    #create a placeholder variable
    placeholder=st.empty()
    credentials_check=False


    with placeholder.form("Login"):
        st.title("Login")
        st.markdown("Please enter your user information")
        user_name=st.text_input("Username", placeholder="Please enter your username")
        password=st.text_input("Password", placeholder="Please enter your password",type='password')
        login_button=st.form_submit_button("Log in")

        if login_button:
            # give warnings if user does not enter anything
            # however there are much better ways to do the authentication, and there is also a library
            if len(user_name) == 0 and len(password) == 0:
                st.warning('Please enter username and password', icon="⚠️")
            elif len(user_name) == 0:
                st.warning('Please enter username', icon="⚠️")
            elif len(password) == 0:
                st.warning('Please enter password', icon="⚠️")
            # only if user enters username and password do we get to this stage
            elif user_name == "test" and password=="test":
                credentials_check = True
            else:
                st.error("Incorrect user/password combination")

    if credentials_check:
        placeholder.empty()
        user_profile_page()

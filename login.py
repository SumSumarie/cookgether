import streamlit as st
from user_profile import user_profile_page
from data_help import connect_to_data, fetch_data

def login_page():
    #create a placeholder variable
    placeholder=st.empty()
    credentials_check=False

    # create database in deta
    db = connect_to_data(db_name="profile")

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
            else:
                # check if user name exists
                # to validate the uniqueness of the user_name
                # use the fetch function to fetch and
                user_data = fetch_data(db)
                user_names = list(user_data.user_name)

                # if user name is found then check the password
                if user_name in user_names:
                    # check password
                    registered_password = list(user_data[user_data["user_name"] == user_name]["password"])[0]

                    if registered_password == password:
                        check_credentials = True
                    else:
                        st.error('Please enter the CORRECT password', icon="⚠️")
                # else insert the user - however, could also add a user name validation step
                else:
                    # to insert the data - use the insert function and pass in a dictionary
                    db.insert({"user_name": user_name,
                               "password": password})
                    check_credentials = True

    if credentials_check==True:
        placeholder.empty()
        user_profile_page()

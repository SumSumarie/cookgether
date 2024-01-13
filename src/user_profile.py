import streamlit as st
from src.data_help import connect_to_data, fetch_data

# create database in deta
db = connect_to_data("profile")

def user_profile_page():
    st.title("Profile")
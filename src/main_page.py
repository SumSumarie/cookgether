import streamlit as st
from streamlit_option_menu import option_menu
from src.community_new import community_upload
from src.recipe_generator import recipe_generator_page
from src.food_share import food_share_page
from src.user_profile import user_profile_page
from src.about import about_page

# REMOVE THIS CODE
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
###

def main_page():

    # 1. as sidebar menu
    with st.sidebar:
        choice = option_menu("Cookgether",
                             ["🥘  Community",
                              "🗒️  AI Recipe Generator",
                              "🍎  Food Share",
                              "😀  Profile",
                              "📌  About"],
                             # create a menu bar
                                menu_icon="house", default_index=1)


    #if else statement to go to different pages
    #the page Community
    if choice =="🥘  Community":
        community_upload()


    #the page AI Recipe Generator
    elif choice =="🗒️  AI Recipe Generator":
        #login_page()
        recipe_generator_page()

    #the page Food Share
    elif choice =="🍎  Food Share":
        food_share_page()

    #the page Food Share
    elif choice =="😀  Profile":
        user_profile_page()


    #the page About
    elif choice =="📌  About":
        about_page()

if __name__ == "__main__":
    main()

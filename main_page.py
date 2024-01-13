import streamlit as st
from streamlit_option_menu import option_menu
from community import community_page
from recipe_generator import recipe_generator_page
from cost_calculator import cost_calculator_page
from food_share import food_share_page
from about import about_page



#code to config the page
st.set_page_config(
    page_title="Cookgether",
    page_icon="🥘"
)


# 1. as sidebar menu
with st.sidebar:
    choice = option_menu("Cookgether", ["🥘  Community", "🗒️  AI Recipe Generator", "🧾  Cost Calculator","🍎  Food Share", "📌  About"],
                         # create a menu bar
                            menu_icon="house", default_index=1)


#if else statement to go to different pages
#the page Community
if choice =="🥘  Community":
    community_page()


#the page AI Recipe Generator
elif choice =="🗒️  AI Recipe Generator":
    recipe_generator_page()

#the page Cost Calculator
elif choice =="🧾  Cost Calculator":
    cost_calculator_page()

#the page Food Share
elif choice =="🍎  Food Share":
    food_share_page()


#the page About
elif choice =="📌  About":
    about_page()


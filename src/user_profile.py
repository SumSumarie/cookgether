import streamlit as st
from src.helper import connect_to_deta, fetch_data

# create database in deta
db = connect_to_deta("profile")
user1 = {
    "username": "Mr.Crabs",
    "email": "mrcrabs@email.com",
    "aboutme": "Hey there! I'm Alex, and cooking is my jam. Seriously, there's nothing I love more than experimenting in the kitchen. My friends call me a flavor wizard because I'm always mixing up spices and herbs, trying to find that perfect taste. I'm big on homemade meals and rarely do takeout. Weeknights are for quick stir-fries or pasta, but weekends are where the magic happens. That's when I dive into slow-cooked roasts or try out some fancy new dessert. I'm also a bit of a cookbook collector and love getting inspiration from them. Oh, and my guilty pleasure? Perfecting the art of the ultimate sandwich. Simple joys, right?",
    "cookinglevel": "Not yet selected",
    "favouritecuisine": "Not yet selected.",
    "dietarypreferences": "Not yet selected.",
    "location": "Berlin",
    "recipes":[]
}

user2 = {
    "username": "Spongebob",
    "email": "spongebob@email.com",
    "aboutme": "Hi! I'm Jordan, and I've got a green thumb for gardening. Nothing beats the satisfaction of growing my own veggies and herbs. You'll often find me outside, tending to my garden with care. My kitchen experiments usually start from whatever's fresh and ready in the garden. Think homemade pesto with basil, or a hearty veggie stew. I love the idea of farm-to-table eating, and I try to live by it. Weekends are my experiment days – maybe trying out a new veggie burger recipe or baking a pumpkin pie from scratch. And I'm all about sharing – my friends love my garden-to-table dinner parties. Gardening and cooking, that's my kind of bliss!",
    "cookinglevel": "Advanced Home Cook 🔪",
    "location": "Hamburg"
}

user_profiles = {
    "Mr.Crabs": user1,
    "Spongebob": user2
}

def user_profile_page():
    st.title("Profile")

    # about me section
    st.subheader('About Me', divider='rainbow')
    st.markdown(user_profiles["Mr.Crabs"]["aboutme"])

    # cooking preferences section
    st.subheader('Cooking Info and Preferences', divider='rainbow')
    st.markdown(f"*My Cooking Level: :green[{user_profiles['Mr.Crabs']['cookinglevel']}]*")
    st.markdown(f"*My Favourite Cuisine: :green[{user_profiles['Mr.Crabs']['favouritecuisine']}]*")
    st.markdown(f"*My Diet: :green[{user_profiles['Mr.Crabs']['dietarypreferences']}]*")

    # generated recipes
    st.subheader('History of recipes:', divider='rainbow')
    for recipe in user1["recipes"]:
        with st.expander("Show the input used for this recipe:"):
            st.write(recipe['prompt'])
        st.markdown(f"*Name:* {recipe['name']}   \n *Cooked on the:* {recipe['date']}  \n *Instructions:* {recipe['instructions']}")
        st.markdown("---")
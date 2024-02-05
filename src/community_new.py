import streamlit as st
from PIL import Image
from src.user_profile import user1

def community_upload():
    st.markdown("Share your generated recipe and your cooking experience")
    recipe_list = [recipes['name'] for recipes in user1['recipes']]

    selected_recipe = st.selectbox(
        'Which recipe do you want to share?',
        recipe_list
    )

    for recipe in user1['recipes']:
        if recipe['name'] == selected_recipe:
            recipe_to_show = recipe

    #with st.expander("Show the recipe instructions:"):
        #st.write(recipe_to_show['instructions'])

    # Upload Image
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Text Input
    user_text = st.text_area("What was you interesting Cookgether experience?")

    # Display Image
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Cookgether", use_column_width=True)

    # Display Text
    if user_text:
        st.write("What was your interesting Cookgether experience?:", user_text)
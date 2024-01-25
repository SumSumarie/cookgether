import streamlit as st
from PIL import Image
import io
from src.user_profile import user1

user_submitted_recipes = []

def community_page():
    st.title("Community")

    st.markdown("Share your generated recipe and your cooking experience")
    recipe_list = [recipes['date'] for recipes in user1['recipes']]

    selected_recipe = st.selectbox(
        'Which recipe do you want to share?',
        recipe_list
    )

    for recipe in user1['recipes']:
        if recipe['date'] == selected_recipe:
            recipe_to_show = recipe

    with st.expander("Show the recipe instructions:"):
        st.write(recipe_to_show['instructions'])


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


    # Submit Button
    if st.button("Submit Recipe"):
        if uploaded_image is not None and user_text:
            # Convert the uploaded file to bytes for storage
            image_bytes = io.BytesIO(uploaded_image.getvalue())
            user_recipe = {
                "image": image_bytes,
                "text": user_text,
                "recipe": recipe_to_show
            }
            user_submitted_recipes.append(user_recipe)

    # Display Submitted Recipes
    for submitted_recipe in user_submitted_recipes:
        # Define the number of columns and rows
        num_columns = 3
        recipe_name="recipe"
        num_rows = len(recipe_name) // num_columns + (len(recipe_name) % num_columns > 0)

        for row in range(num_rows):
            recipe_columns = st.columns(num_columns)

            for col in range(num_columns):
                recipe_index = row * num_columns + col
                if recipe_index < len(recipe_name):
                    with recipe_columns[col]:
                        #file_path = image_path[recipe_index]

                        food_image = st.image(Image.open(submitted_recipe["image"]), caption=submitted_recipe["text"], use_column_width=True)

        #st.image(Image.open(submitted_recipe["image"]), caption="User Recipe", use_column_width=True)
        st.write("User Experience:", submitted_recipe["text"])
        st.write("Recipe Instructions:", submitted_recipe["recipe"]["instructions"])

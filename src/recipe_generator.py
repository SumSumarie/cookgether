import streamlit as st
from datetime import datetime
from openai import OpenAI
from src.user_profile import user1


client = OpenAI(api_key=st.secrets['open_api_key'])
def recipe_generator_page():
    #st.title("AI Recipe Generator")

    # set OpenAI API key

    # set up the .streamlit page
    #st.set_page_config(page_title="Recipe Generator")

    # basic info
    st.title("Recipe Generator")

    ingredients = st.multiselect(
        'Which ingredients do you have at hand?',
        ('Tomatoes 🍅',
         'Lettuce 🥬',
         'Cheese 🧀',
         'Chicken 🍗',
         'Beef 🥩',
         'Fish 🐟',
         'Eggs 🥚',
         'Onions 🧅',
         'Garlic 🧄',
         'Mushrooms 🍄',
         'Potatoes 🥔',
         'Carrots 🥕',
         'Rice 🍚',
         'Pasta 🍝',
         'Bread 🍞')
    )

    with st.expander("Want to add more ingredients?"):
        additional_ingredients = st.text_input("Any other ingredients you have at hand?")

    cuisine = st.selectbox(
        'Which cuisine do you prefer the most?',
        ('Italian 🤌🇮🇹',
         'Chinese 🍚🇨🇳',
         'Japanese 🍣🇯🇵',
         'Mexican 🌮🇲🇽',
         'Indian 🍛🇮🇳',
         'Thai 🍜🇹🇭',
         'French 🥐🇫🇷',
         'Greek 🥙🇬🇷',
         'Spanish 🥘🇪🇸',
         'Korean 🥢🇰🇷')
    )

    cookingappliances = st.multiselect(
        'Which cooking appliances do you have in your kitchen and would use for cooking?',
        ('Oven',
         'Air Fryer',
         'Microwave',
         'Blender',
         'Toaster',
         'Slow Cooker',
         'Pressure Cooker',
         'Food Processor',
         'Grill',
         'Stove')
    )

    numberofpeople = st.number_input("How many people are you cooking for?", min_value=0, max_value=None, value=0,
                                     step=1)

    cookingtime = st.select_slider(
        'How much time would you spent on Cooking today?',
        options=['5', '15', '30', '45', '60', '90', '∞'])

    cookinglevel = st.select_slider(
        'How would you rate your own cooking level?',
        options=['Absolute Beginner👶', 'Basic Cooking 🍳', 'Advanced Home Cook 🔪', 'Professional Chief 👨‍🍳'])

    with st.expander("Any other dietary needs we have to know about? (Vegetarian, Vegan etc?)"):
        # Define the dietary options
        dietary_options = ['Vegan', 'Vegetarian', 'Pescatarian', 'Omnivore']

        # Create an empty list to store the user's selections
        selected_dietary_preferences = []

        # Iterate over the options and create a checkbox for each
        for option in dietary_options:
            if st.checkbox(option):
                selected_dietary_preferences.append(option)

        # Join the selected options into a single string
        dietary_preferences_str = ', '.join(selected_dietary_preferences)

    # handling the user input
    if st.button('Generate Recipe'):
        # Generating a prompt based on the ingredients while preserving original input
        recipe_prompt = (
            f"Please generate one detailed recipe with step-by-step instructions that meets all of the following requirements:"
            f"\n\nIngredients:"
            f"\n- Include as many as possible of: {ingredients} {additional_ingredients}"
            f"\n\nDietary Preferences: "
            f"\n- {dietary_preferences_str}" 
            f"\n\nCuisine Preference:"
            f"\n- {cuisine} "
            f"\n\nTimeframe: "
            f"\n- The recipe should take around {cookingtime} minutes from start to finish."
            f"\n\nServing Size:" 
            f"\n- The recipe should serve {numberofpeople} people."
            f"\n\nCooking Level:"
            f"\n- The recipe should be appropriate for someone at a {cookinglevel} cooking level."
            f"\n\nCooking Appliances:"
            f"\n- Only use the following appliances: {cookingappliances}"
            f"\n\nFormat:"
            f"\n- Start with a detailed ingredients list"
            f"\n- Then provide step-by-step instructions for preparing the recipe"
        )
        with st.expander("Show the prompt used for this recipe:"):
            st.write('This is the current prompt', recipe_prompt)
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": f"{recipe_prompt}"}])
        # recipe_output = response['choices'][0]['message']['content']
        recipe_output = response.choices[0].message.content

        name = client.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=[{"role": "system", "content": f"Generate a short name for the following recipe with an Emoji attached, consider that it is a {cuisine} recipe for your title. The recipe: {recipe_output}"}])
        name_output = name.choices[0].message.content

        # display recipe output
        st.info(f"*Name:*   \n{name_output}   \n   \n{recipe_output}")

        # generate a structured recipe with original ingredients and the date of generation
        today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        topic = f"Based on your ingredients: {ingredients} I created this recipe for you \n{recipe_output}"
        filename = f"Recipe_from_{today}.txt"

        st.download_button(
            label="Download Recipe",
            data=topic,
            file_name=filename
        )

        input_summary = (
            f"**Selected Ingredients:** {', '.join(ingredients)}   \n"
            f"**Additional Ingredients:** {additional_ingredients}   \n"
            f"**Preferred Cuisine:** {cuisine}   \n"
            f"**Available Cooking Appliances:** {', '.join(cookingappliances)}   \n"
            f"**Number of People:** {numberofpeople}   \n"
            f"**Cooking Time:** {cookingtime}   \n"
            f"**Cooking Level:** {cookinglevel}   \n"
            f"**Dietary Preferences:** {dietary_preferences_str}   \n"
        )

        new_recipe = {
            "date": today,
            "name": name_output,
            "ingredients": ingredients,
            "instructions": recipe_output,
            "prompt": input_summary
        }

        user1["recipes"].append(new_recipe)

    # update preferences to user profile
    newpreferences = {
        "cookinglevel": cookinglevel,
        "favouritecuisine": cuisine,
        "dietarypreferences": dietary_preferences_str
    }

    user1.update(newpreferences)
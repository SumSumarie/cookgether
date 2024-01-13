import streamlit as st
from datetime import datetime
from openai import OpenAI

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
        recipe_prompt = f"Generate one recipe based on all the requirements below (ONLY ONE! But make it detailed. Always start with a ingredients part and then a detailed step by step guide! These are my prerequisites: " \
                        f"My ingredients, please include as many as possible: {ingredients} {additional_ingredients}. " \
                        f"My dietary preferences are: {dietary_preferences_str}." \
                        f"My favourite cuisine: {cuisine}. " \
                        f"This timeframe I have for cooking: {cookingtime} minutes. " \
                        f"The number of people I am cooking for {numberofpeople}. " \
                        f"The Cooking Level i am currently am: {cookinglevel}. " \
                        f"Make sure that the recipe is possible with just the following cooking appliances: {cookingappliances}. "
        with st.expander("Show the prompt used for this recipe:"):
            st.write('This is the current prompt', recipe_prompt)
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": f"{ingredients}"}])
        # recipe_output = response['choices'][0]['message']['content']
        recipe_output = response.choices[0].message.content

        # display recipe output
        st.info(recipe_output)

        # generate a structured recipe with original ingredients and the date of generation
        today = datetime.today().strftime('%Y-%m-%d')
        topic = f"Based on your ingredients: {ingredients} I created this recipe for you \n{recipe_output}"
        filename = f"Recipe_from_{today}.txt"

        st.download_button(
            label="Download Recipe",
            data=topic,
            file_name=filename
        )




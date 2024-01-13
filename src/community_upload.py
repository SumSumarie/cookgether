import streamlit as st
from PIL import Image

st.title("Your Cookegether experience")

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

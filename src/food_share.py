import streamlit as st
import requests


def get_content():
    """Access the API and get the image URL"""
    #should change to the food API
    contents=requests.get('https://cataas.com//cat')
    return contents.content

def food_share_page():
    st.title("Food Share")

    row1 = st.columns(3)
    row1_1=st.columns(3)
    row2 = st.columns(3)
    row2_1 = st.columns(3)
    row3 = st.columns(3)
    row3_1 = st.columns(3)
    row4 = st.columns(3)
    row4_1 = st.columns(3)
    row5 = st.columns(3)
    row5_1 = st.columns(3)



    for col in row1 + row2 +row3+ row4 +row5:
        food_image = get_content()
        tile = col.container(height=200)
        tile.image(food_image, width=200)

    for col in row1_1 + row2_1 + row3_1 + row4_1 +row5_1:
        col.caption('food')
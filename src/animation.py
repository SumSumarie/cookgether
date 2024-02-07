import streamlit as st
from streamlit_lottie import st_lottie
import time

def cooking_animation(H,W):
    st_lottie_url = "https://lottie.host/5e40c7d4-3253-4ac8-9a96-4a3575da91f5/V4LHvS4XDN.json"
    # Show Lottie animation
    animation_placeholder = st.empty()
    st_lottie(st_lottie_url, height=H, width=W)
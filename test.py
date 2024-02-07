import streamlit as st
from streamlit_lottie import st_lottie
import time

with st.empty():
        st_lottie_url = "https://lottie.host/5e40c7d4-3253-4ac8-9a96-4a3575da91f5/V4LHvS4XDN.json"
        # Show Lottie animation
        animation_placeholder = st.empty()
        st_lottie(st_lottie_url, height=100, width=100)
        time.sleep(1)
        st.write("✔️ 1 minute over!")


from deta import Deta
import streamlit as st
import pandas as pd

def connect_to_data(base_name):
    """This connect to deta and creates a data base to store our data"""
    deta=Deta(st.secrets["data_key"])


    db=deta.Base(base_name)
    return db


def fetch_data(db):
    return pd.DataFrame(db.fetch().items)
import streamlit as st
from deta import Deta

# This is the form that will collect the information we want to write to the deta base
with st.form("form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age")
    submitted = st.form_submit_button("Store in database")


# Connect to Deta Base with your Data Key
deta = Deta(st.secrets["data_key"])

# Create a new database "example-db"
db_name = "test-db" # you can adjust this every time you want to store your data in a new database
# If you need a new database, just use another name.
db = deta.Base(db_name)

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "age": age})
    st.success("Your data has been stored, thanks :)")

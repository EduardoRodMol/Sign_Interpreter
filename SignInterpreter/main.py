import streamlit as st
from pages.partida import app
from pages.desarrolla import dev_w_us
from pages.home import home
from pages.how import how

st.set_page_config(page_title="Sign_Interpreter", layout="wide")

st.title("Sign_Interpreter Project")
page = st.sidebar.radio("Page selected", ["Main Page","Game","Develop with us", "How does it works?"])

if page == "Main Page":
    
    home()
if page == "Game":
    app()

if page == "Develop with us":
   dev_w_us()

if page == "How does it works?":
   how()

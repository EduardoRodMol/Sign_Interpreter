import streamlit as st
import os
from PIL import Image

def dev_w_us():  
    st.text("In this area you wil be able to create your own sign")
    st.text("For using this application on your local device, first of all clone the repository")
    url = "https://github.com/SignInterpreter/Agora"
    st.markdown("this repository [link](%s)" % url)
    st.text("install the dependencies detailed in the requirements file ")
    st.text("and after that you will be able to create your own dataset with the sign that you prefer, running the command ")
    rutaimg = os.path.join(os.getcwd(),"img") 
    image = Image.open(rutaimg+'\getdata.jpg')
    st.image(image, caption='Sunrise by the mountains')


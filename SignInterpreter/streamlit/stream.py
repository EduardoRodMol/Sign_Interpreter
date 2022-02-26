import streamlit as st
from streamlit.label import *

st.title("OpenCV Demo App")
st.subheader("This app allows you to play the classic Stone, Paper & Scissors !")
st.text("We use OpenCV and Streamlit for this demo")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
    
if st.checkbox("Main Checkbox"):
    st.text("Check Box Active")

slider_value = st.slider("Slider", min_value=0.5, max_value=3.5)
st.text(f"Slider value is {slider_value}")

st.sidebar.text("text on side panel")
st.sidebar.checkbox("Side Panel Checkbox")
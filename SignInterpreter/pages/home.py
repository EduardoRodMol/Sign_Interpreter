import streamlit as st


def home():
    st.subheader("Summary")
    st.text("This project would provide an efficient sign interpreter through your camera device")
    st.text('Our first goal consists of developing the classic game "stone, paper, scissors"')
    st.text('Enjoy playing a match against the computer clicking on the "Game" select option of the sidebar')
   
  
  
    st.subheader("Dataset")
    st.text("The dataset has been created by us, using mediapipe and opencv.")
    st.text("Capturing the images of both hands and storing them with its matching label.")
    st.text("We invite you to create your own sign and added it to the neuronal net clicking on Develop with us.")




    st.subheader("Developers")
    st.markdown("Eduardo Rodriguez => https://github.com/EduardoRodMol")
    st.markdown("Borja Espés => https://github.com/BorjaEACode")


import streamlit as st
from wbrtc.videoprocesador import  videoweb#,VideoProcessor,
#from streamlit_webrtc import webrtc_streamer, WebRtcMode

def app():
    
  st.subheader("Welcome to the demo application")
  st.subheader("This app allows you to play the classic Stone, Paper, Scissors !")
  st.text("With this game we want to demostrate that it is possible to teach the signs to the computer ")
  st.text("And we want to evolve this project until the computer will be able to help ")
  st.text("people who are unable to use verbal communication to make themselves understood easier.  ")
  st.text("Do you wanna play? Click on run")
  run = st.checkbox('Run')
  if run:
      
    videoweb()

    
  else:
      st.write('Stopped')
      
  
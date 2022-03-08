
import streamlit as st
from PIL import Image
import os
def how():
    st.subheader(" Do you want to know, how does it works?")
    st.text ("MediaPipe Hands is a high-fidelity hand and finger tracking solution. ")
    st.text("It employs machine learning (ML) to infer 21 3D landmarks of a hand from just a single frame") 
    rutaimg = os.path.join(os.getcwd(),"img") 
    image = Image.open(rutaimg+'\hand_landmarks.jpg')
    image2 = Image.open(rutaimg+'\hand_crops.jpg')
    st.image(image, caption='Sunrise by the mountains')
    st.image(image2, caption='Sunrise by the mountains')
    st.text ("A hand landmark model that operates on the cropped image region defined by the palm detector and returns high-fidelity 3D hand keypoints")
    st.text("Providing the accurately cropped hand image to the hand landmark model drastically reduces the need for data augmentation" )
# # We use mediapipe a hands in order to create a net in our hands 

# Thsi net has 21 point and calcualeate distance between the point n der to calcaulate the , 
#thsi are transform to a arry and this array is includede into a neuronal network. 
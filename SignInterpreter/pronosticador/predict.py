import os
from tensorflow.python.keras.models import load_model
from data.keypoints import mp_holistic, mediapipe_detection, draw_styled_landmarks
from data.values import extract_keypoints
from data.datarecord import actions
import numpy as np


global model 
model = load_model("action.h5")


def extraerkeypoints(img,holistic):   
    image, results = mediapipe_detection(img, holistic)
    draw_styled_landmarks(image, results)
    keypoints = extract_keypoints(results)
    return keypoints





def predice(sequence):
    global model
   
    sentence =[]
    threshold = 0.8
    res = model.predict(np.expand_dims(sequence, axis=0))[0]
    if res[np.argmax(res)] > threshold: 
            if len(sentence) > 0: 
                if actions[np.argmax(res)] != sentence[-1]:
                    sentence.append(actions[np.argmax(res)])
            else:
                sentence.append(actions[np.argmax(res)])
    if len(sentence) > 5: 
        sentence = sentence[-5:]

    return sentence

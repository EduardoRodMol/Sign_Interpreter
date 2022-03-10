from data.keypoints import mp_holistic,mediapipe_detection, draw_styled_landmarks
from data.datarecord import actions
from data.values import extract_keypoints
from pronosticador.predict import  predice, extraerkeypoints
import asyncio

global sequence2 
sequence2 = []


#originally the model was trained in order to recover 30 frames and create predicction witrh movement
#as the time that we have for the project is only 2 weeks 
#we have take the decision of use an static image to recreate the necesary shape for the model.
#this is the reason why the sequence2 add 30 times the same keypoint.


def get_datapoint(frame):
   
    global sequence2
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        keypoint=  extraerkeypoints(frame,holistic)               
        while len(sequence2)!=30:
            sequence2.append(keypoint)                    
        sequence2 = sequence2[-30:]                
    return sequence2


def get_pronostico(sequence):
    
    if len(sequence) == 30: 
        global sequence2 
        sequence2 = []                   
        sentence = predice(sequence)
        if  sentence:           
            sentence =str(sentence[0].replace("['","").replace("']",""))
        
        print("Running inference..."+str(sentence))
        return str(sentence)
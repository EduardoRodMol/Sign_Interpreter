from data.keypoints import mp_holistic,mediapipe_detection, draw_styled_landmarks
from data.datarecord import actions
from data.values import extract_keypoints
from pronosticador.predict import  predice, extraerkeypoints


global sequence2 
sequence2 = []


def get_datapoint(frame):

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        global sequence2                
        while len(sequence2)!=30:
            print(len(sequence2))
            sequence2.append(extraerkeypoints(frame,holistic))

        sequence2 = sequence2[-30:]
        print("secuence2 "+ str(len(sequence2)) )
        
        return sequence2


def get_pronostico(sequence):
    sentence= "getting info"
    if len(sequence) == 30: 
        global sequence2 
        sequence2 = []                   
        sentence = predice(sequence)
        print("Running inference..."+str(sentence))
        return str(sentence)
import os
from tensorflow.python.keras.models import load_model
from data.keypoints import mp_holistic, mediapipe_detection, draw_styled_landmarks
from data.values import extract_keypoints
from data.datarecord import actions
import numpy as np
import cv2

def predice(loteimg,holistic):

    model = load_model("action.h5")
    sequence=[]
    sentence =[]
    threshold = 0.8
    for img in loteimg:
        image, results = mediapipe_detection(img, holistic)
        draw_styled_landmarks(image, results)
        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-30:]
            #self.contador = self.contador +1
        print ("hola" )
        print("longitud" + str(len(sequence)))
        print(keypoints)
        
        if len(sequence) == 10:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            label = actions[np.argmax(res)]
            print (label)
           
            if res[np.argmax(res)] > threshold: 
                    if len(sentence) > 0: 
                        if actions[np.argmax(res)] != sentence[-1]:
                            sentence.append(actions[np.argmax(res)])
                    else:
                        sentence.append(actions[np.argmax(res)])

            if len(sentence) > 5: 
                sentence = sentence[-5:]
        
 #       await producer.send_and_wait(topic_name, label) # Define a topic when you send a message
                                                        # This way, they can be sorted by different consumers
    return label



def update_cv2(img,label):
         cv2.rectangle(img, (0,0), (640, 40), (245, 117, 16), -1)
         cv2.putText(img, ' '.join(label), (3,30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
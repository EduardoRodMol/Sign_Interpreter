from streamlit_webrtc import webrtc_streamer, WebRtcMode,VideoProcessorBase
import av
from tensorflow.python.keras.models import load_model
from data.keypoints import mp_holistic, mediapipe_detection, draw_styled_landmarks
from data.values import extract_keypoints
from data.datarecord import actions
import cv2
import numpy as np
import queue
#from streamlit.rtc_configuration import RTC_CONFIGURATION
#from aiortc.contrib.media import MediaPlayer
model = load_model("action.h5")
import queue


def process_kafka_message():^
    image, results = mediapipe_detection(img, holistic)
    # ... extract from buffer of 10 images receive from kafka message
    draw_styled_landmarks(image, results)
    keypoints = extract_keypoints(results)
    self.sequence.append(keypoints)
    self.sequence = self.sequence[-10:]
    #self.contador = self.contador +1
    print ("hola" )
    print("longitud" + str(len(self.sequence)))
    print(keypoints)

    if len(self.sequence) == 10:
        res = self.model.predict(np.expand_dims(self.sequence, axis=0))[0]
        label = actions[np.argmax(res)]
        print(label)


def consume_kafka_results():^
    # consume mensajes del topic de kafka donde se emiten resultados y actualiza la variable global

global kafka_prediciton = "üunknown"

class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.model = load_model("action.h5")
        self.sequence = []
        self.predict_threshold = 50
        self.frame_count = 0

    def recv(self, frame: av.VideoFrame) :
        threshold = 0.8
        
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            img = frame.to_ndarray(format="bgr24")
            self.sequence.append(img)
            self.sequence = sequence[-10:]
            if self.frame_count > self.predict_threshold:^
                self.frame_count = 0
                # Send self.sequence to kafka topic
            else:
                self.frame_count += 1
            #cada 50 recepciones mando la lieta de los ultimos 10
            #consumer de kafka
            
            #consumer kafka de cada 24 frames consume 1
            # kaka actualiza la variable  global 
        #flipped = img[::-1,:,:]¨
        # with opencv write text on global variable ka_fa_predicion in image

        return av.VideoFrame.from_ndarray(image, format="bgr24")

ctx =webrtc_streamer(
    key="Sign_Interpreter",
    mode=WebRtcMode.SENDRECV,
   # rtc_configuration=RTC_CONFIGURATION,
    video_processor_factory=VideoProcessor
    )
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




class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.model = load_model("action.h5")
        self.sequence = []

    def recv(self, frame: av.VideoFrame) :
        #sequence = []
        threshold = 0.8
        
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            img = frame.to_ndarray(format="bgr24")
            image, results = mediapipe_detection(img, holistic)
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

        #flipped = img[::-1,:,:]

        return av.VideoFrame.from_ndarray(image, format="bgr24")

ctx =webrtc_streamer(
    key="Sign_Interpreter",
    mode=WebRtcMode.SENDRECV,
   # rtc_configuration=RTC_CONFIGURATION,
    video_processor_factory=VideoProcessor
    )
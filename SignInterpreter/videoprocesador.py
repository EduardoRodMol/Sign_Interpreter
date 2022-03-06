#import sys
#sys.path.append("../")
from streamlit_webrtc import webrtc_streamer, WebRtcMode,VideoProcessorBase
import av

import cv2
import numpy as np
import queue
from strem.predict import predice
from data.keypoints import mp_holistic
#from strem.rtc_config import RTC_CONFIGURATION
#from aiortc.contrib.media import MediaPlayer

import queue
import asyncio




def consume_kafka_results():
    pass
    # consume mensajes del topic de kafka donde se emiten resultados y actualiza la variable global

#global kafka_prediciton = "continua"


class VideoProcessor(VideoProcessorBase):
    def __init__(self):
       # self.model = load_model("action.h5")
        self.sequence = []
        self.predict_threshold = 30
        self.frame_count = 0
        self.label = ""
        self.pronostico= ""
    
        
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        #threshold = 0.8
        
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            img =  frame.to_ndarray(format="bgr24")
            cv2.rectangle(img, (0,0), (640, 40), (245, 117, 16), -1)
            cv2.putText(img, ' '.join(self.label), (3,30), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA) 
                
            self.sequence.append(img)
            self.sequence = self.sequence[-30:]
            if self.frame_count > self.predict_threshold:
                self.frame_count = 0
                #enviamos las imagenes al modelo pra predecir                                        
                self.label =predice(self.sequence, holistic)
                print(self.label)
                #escribimos la imagen
                #self.pronostico = self.pronostico +", "+ self.label
            
                    # Send self.sequence to kafka topic
            else:
                self.frame_count += 1
                #cada 50 recepciones mando la lieta de los ultimos 10
                #consumer de kafka
                
                #consumer kafka de cada 24 frames consume 1
                # kaka actualiza la variable  global 
            #flipped = img[::-1,:,:]¨
            # with opencv write text on global variable ka_fa_predicion in image
            
            
            ####DEVOLVEMOS IMG, PERO DEVERIAMOS DEVULVER IMAGE, con la pitnura
            
            
        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_ctx =webrtc_streamer(
    key="Sign_Interpreter",
    mode=WebRtcMode.SENDRECV,
    #rtc_configuration=RTC_CONFIGURATION,
    video_processor_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True
    )

'''
web streamer es quien hace la conexion con los objetos de la web para aplicarlos al modelo

if webrtc_ctx.video_processor:
    webrtc_ctx.video_processor.confidence_threshold = confidence_threshold
'''
   
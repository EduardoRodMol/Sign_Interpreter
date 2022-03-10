#import sys
#sys.path.append("../")
from streamlit_webrtc import VideoProcessorBase,webrtc_streamer, WebRtcMode
import av
from juego.game import juego
import cv2
import numpy as np
import queue
from pronosticador.predict import extraerkeypoints, predice,update_cv2
from data.keypoints import mp_holistic
from wbrtc.datapoint import get_datapoint,get_pronostico
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
        self.predict_threshold = 35
        self.frame_count = 0
        self.label = "ready?"
        self.pronostico= ""
        
    
    
    
    
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:

        #with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        img =  frame.to_ndarray(format="bgr24")
        self.sequence = get_datapoint(img)
        print(self.frame_count)     
        update_cv2(img,"getting information "+str(self.frame_count)+ " of 30")  
        print("secuence self lon "+str(len(self.sequence))+ " of 30")       
        if len(self.sequence)== 30:
            self.frame_count = 0
            print(self.frame_count)  
            self.pronostico = get_pronostico(self.sequence)
            print(type(self.pronostico))
            self.sequence = []
            print(len(self.sequence))
            print(self.pronostico)
            if self.pronostico != "":
                #print(str(self.pronostico[0])) 
                print(str(self.pronostico))                
                if str(self.pronostico) in ("piedra","papel","tijera"):
                    self.label = juego(str(self.pronostico))
                    print(self.label)
                    update_cv2(img,str(self.label))

            # update_cv2(img,str(self.label))
            # self.sequence.append(extraerkeypoints(img,holistic))
            # self.sequence = self.sequence[-30:]
            # print("llevamos: " + str(self.frame_count))
            # if self.frame_count > self.predict_threshold:
            #     self.frame_count = 0
            #     #enviamos las imagenes al modelo pra predecir  
            #     self.label = "calculando"
            #     print("calculando")                                                  
            #     self.pronostico = predice(self.sequence, holistic)
            #     print(self.pronostico)
            #     print(type(self.pronostico))
            #     self.label = self.pronostico            
            #     #update_cv2(img,self.label)
            #     print(str(self.label))
                
                    # Send self.sequence to kafka topic
        else:
            self.frame_count += 1
                
                
                #consumer kafka de cada 24 frames consume 1
                # kaka actualiza la variable  global 
            
            # with opencv write text on global variable ka_fa_predicion in image
            
            
            
            
        return av.VideoFrame.from_ndarray(img, format="bgr24")

def videoweb():
    webrtc_ctx =webrtc_streamer(
        key="Sign_Interpreter",
        mode=WebRtcMode.SENDRECV,
        #rtc_configuration=RTC_CONFIGURATION,
        video_processor_factory=VideoProcessor,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True
        )



#import sys
#sys.path.append("../")
from streamlit_webrtc import VideoProcessorBase,webrtc_streamer, WebRtcMode
import av
from juego.game import juego
import cv2
import numpy as np
import queue
from predict import extraerkeypoints, predice,update_cv2
from data.keypoints import mp_holistic
#from strem.rtc_config import RTC_CONFIGURATION
#from aiortc.contrib.media import MediaPlayer
from vinterprete.kafkauser.producer import kafkakeypoints
import queue
import asyncio
from threading import Thread


def consume_kafka_results():
    pass
    # consume mensajes del topic de kafka donde se emiten resultados y actualiza la variable global

#global kafka_prediciton = "continua"


class VideoProcessor(VideoProcessorBase):
    def __init__(self):
       # self.model = load_model("action.h5")
        self.sequence = []
        self.predict_threshold = 40
        self.frame_count = 0
        self.label = "ready?"
        self.pronostico= ""
        
    
    
    
    
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:

        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            img =  frame.to_ndarray(format="bgr24")
            update_cv2(img,self.label)
            #nos llevamos la imagen y holistic para sacar los keypoints
            print("ahora")
            # thread = RunThread(kafkakeypoints, img,holistic)
            # thread.start()
            # thread.join()
            kafkakeypoints(img,holistic)
          
            print("fuera")
            self.sequence.append(extraerkeypoints(img,holistic))
            self.sequence = self.sequence[-30:]
            
            if self.frame_count > self.predict_threshold:
                self.frame_count = 0                 
                self.label = "calculando"
                print("calculando")                                                    
                self.pronostico = predice(self.sequence, holistic)
                print(self.pronostico)
                print(type(self.pronostico))
                self.label = self.pronostico            
                print(str(self.label))
                self.label = juego(str(self.pronostico))
                print(self.label)
                update_cv2(img,self.label)
                    # Send self.sequence to kafka topic
            else:
                self.frame_count += 1
                
            
            
        return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_ctx =webrtc_streamer(
    key="Sign_Interpreter",
    mode=WebRtcMode.SENDRECV,
    #rtc_configuration=RTC_CONFIGURATION,
    video_processor_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True
    )




# '''
# web streamer es quien hace la conexion con los objetos de la web para aplicarlos al modelo

# if webrtc_ctx.video_processor:
#     webrtc_ctx.video_processor.confidence_threshold = confidence_threshold
# '''
   
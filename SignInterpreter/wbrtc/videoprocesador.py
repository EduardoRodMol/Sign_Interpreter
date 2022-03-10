from streamlit_webrtc import VideoProcessorBase,webrtc_streamer, WebRtcMode
import av
from juego.game import juego
import numpy as np
from wbrtc.print import update_cv2,escribeppt
from wbrtc.datapoint import get_datapoint,get_pronostico
import asyncio
import time


class VideoProcessor(VideoProcessorBase):
    def __init__(self):
       # self.model = load_model("action.h5")
        self.sequence = []
        self.predict_threshold = 35
        self.frame_count = 0
        self.label = "ready?"
        self.pronostico= ""
        

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        
        img =  frame.to_ndarray(format="bgr24")
        print(self.frame_count)
        self.frame_count += 1
        if self.frame_count <20:
            update_cv2(img,"Stone")
        if self.frame_count >19:
            if self.frame_count <40:
                update_cv2(img,"Paper")
            if  self.frame_count >39:
                update_cv2(img," or Scissors!!!")
        if self.frame_count >50:
            update_cv2(img,"")

        if self.frame_count == 53:
            escribeppt(img)
            update_cv2(img,str(self.label))
            self.sequence = get_datapoint(img)
            print(self.sequence)                
            if len(self.sequence)== 30:
                
                #pendiente un contador de partidas
                #self.frame_count = 0
                #self.frame_count += 1
                self.pronostico = get_pronostico(self.sequence)            
                self.sequence = []
                print(self.pronostico)
                if self.pronostico != "":                                        
                    if str(self.pronostico) in ("piedra","papel","tijeras"):
                        self.label = juego(str(self.pronostico))
                        print (str(self.label))
                        update_cv2(img,str(self.label))
                       
        if self.frame_count > 53:
            update_cv2(img,str(self.label))
         
        if self.frame_count > 80:
            self.frame_count = 0
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



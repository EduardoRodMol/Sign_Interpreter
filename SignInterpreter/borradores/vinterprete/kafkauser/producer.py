
from vinterprete.producer.producer import send
from data.keypoints import mp_holistic, mediapipe_detection, draw_styled_landmarks
from data.values import extract_keypoints
import asyncio
from threading import Thread

class RunThread(threading.Thread):
    def __init__(self, func, img, holistic):
        self.func = func
        self.ing = img
        self.hoistic = holistic
        threading.Thread.__init__()

    def run(self):
        self.result = asyncio.run(self.func(self.img, self.holistic))

def kafkakeypoints(img,holistic):
       
    image, results = mediapipe_detection(img, holistic)
    draw_styled_landmarks(image, results)
    keypoints = extract_keypoints(results)
    print("en medio")
    asyncio.run(send(keypoints))
    
    
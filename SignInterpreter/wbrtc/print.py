import cv2
from data.datarecord import actions

import time

def update_cv2(img,label):
  
        rectangulo = cv2.rectangle(img, (0,0), (640, 40), (245, 117, 16), -1)
        cv2.putText(rectangulo, ' '.join(label), (3,30),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
    

def escribeppt(img) :
    for label in actions:
        cv2.rectangle(img, (0,0), (640, 40), (245, 117, 16), -1)
        cv2.putText(img, ' '.join(label), (3,30), 
               cv2.FONT_HERSHEY_SIMPLEX                  , 1, (255, 255, 255), 2, cv2.LINE_AA)
        
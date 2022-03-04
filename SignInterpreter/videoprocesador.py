from streamlit_webrtc import webrtc_streamer, WebRtcMode
import av
from tensorflow.python.keras.models import load_model
from data.keypoints import mp_holistic, mediapipe_detection, draw_styled_landmarks
from data.values import extract_keypoints
from data.datarecord import actions
import cv2
import numpy as np



model = load_model("action.h5")


class VideoProcessor:

    def recv(self, frame):
        sequence = []
        sentence = []
        threshold = 0.8
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            img = frame.to_ndarray(format="bgr24")
            image, results = mediapipe_detection(img, holistic)
            draw_styled_landmarks(image, results)
            keypoints = extract_keypoints(results)
            sequence.append(keypoints)
            sequence = sequence[-30:]
            
            if len(sequence) == 30:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]
                print(actions[np.argmax(res)])

        #flipped = img[::-1,:,:]

        return av.VideoFrame.from_ndarray(image, format="bgr24")


webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=VideoProcessor)
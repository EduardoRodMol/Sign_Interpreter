from rtc_config import RTC_CONFIGURATION
import os
import av
from tensorflow.python.keras.models import load_model
from streamlit_webrtc import (
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer
)
from data.keypoints import mediapipe_detection,draw_styled_landmarks
from datarecord import actions
MODEL_PATH= os.getcwd()+"/action.h5"
print(MODEL_PATH)
#segunda prueba
class TensorFlowVideoProcessor(VideoProcessorBase):

    def __init__(self) -> None:
        self._model = load_model(MODEL_PATH)
        self.holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.result_queue = queue.Queue()
        self.keypoint = []
        self.sequence = []
        self.results =[]

       
    def _annotate_image(self, image):

        self.keypoints = extract_keypoints(self.results)
        self.sequence.append(keypoints)
        self.sequence = sequence[-30:]
         
        if len(self.sequence) == 30:
            res = self._model.predict(np.expand_dims(self.sequence, axis=0))[0]
            print(actions[np.argmax(res)])
            if res[np.argmax(res)] > threshold: 
                if len(sentence) > 0: 
                    if actions[np.argmax(res)] != sentence[-1]:
                        self.sentence.append(actions[np.argmax(res)])
                else:
                    self.sentence.append(actions[np.argmax(res)])

            if len(self.sentence) > 5: 
                    self.sentence = sentence[-5:]
                    result = self.sentence

        return image, result

        
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
       
        frame = frame.to_ndarray(format="bgr24")
        #aun no se como meter el holistic
        image, self.results = mediapipe_detection(frame, self.holistic)
        draw_styled_landmarks(image, results)

        '''
        es un preproceso de imagen para meterla en la red
        blob = cv2.dnn.blobFromImage(
            cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
        )
        '''
        '''
        self._net.setInput(blob)
        detections = self._net.forward()
        '''
        image, result = self._annotate_image(image)

        # NOTE: This `recv` method is called in another thread,
        # so it must be thread-safe.
        self.result_queue.put(result)

        return av.VideoFrame.from_ndarray(annotated_image, format="bgr24")


webrtc_ctx = webrtc_streamer(
    key="object-detection",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    video_processor_factory=TensorFlowVideoProcessor,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True
)
'''
web streamer es quien hace la conexion con los objetos de la web para aplicarlos al modelo

if webrtc_ctx.video_processor:
    webrtc_ctx.video_processor.confidence_threshold = confidence_threshold
'''
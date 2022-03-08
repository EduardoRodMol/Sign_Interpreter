from send_frame import connect_kafka, send_frame_kafka
from streamlit_webrtc import VideoProcessorBase, webrtc_streamer, WebRtcMode
from av import VideoFrame
import asyncio


class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.sequence = []
        self.frame_count = 0
        self.label = "ready?"
        self.pronostico = ""
        self.predict_threshold = 100

    def recv(self, frame: VideoFrame) -> VideoFrame:

        # with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        #     img = frame.to_ndarray(format="bgr24")
        #     #update_cv2(img, self.label)

        #     #self.sequence.append(extraerkeypoints(img, holistic))
        #     self.sequence = self.sequence[-30:]

        if self.frame_count > self.predict_threshold:
            send_frame_kafka(frame)
            self.frame_count = 0
        else:
            self.frame_count += 1

        return frame


asyncio.run(connect_kafka())

webrtc_ctx = webrtc_streamer(
    key="Sign_Interpreter",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True
)

from streamlit_webrtc import webrtc_streamer
import av


class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        flipped = img[::-1,:,:]

        return av.VideoFrame.from_ndarray(flipped, format="bgr24")


webrtc_streamer(key="example", video_processor_factory=VideoProcessor)
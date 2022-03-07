from streamlit_webrtc import (
    RTCConfiguration
)

local_turn = "turn:localhost:3478"
local_stun = "stun:localhost:3478"
google_stun = "stun:stun.l.google.com:19302"

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{
        "urls": [google_stun],
        "username":"marc",
        "credential":"marc"
    }]}
)

"""Implementation of a source-type to select a video and apply the Haar Cascade classifier on it"""

# Core Pkgs

import av
import streamlit as st
from streamlit_webrtc import MediaPlayerFactory, WebRtcMode, webrtc_streamer

from pki_a22_app.dashboard.sources import SourcesInterface
from pki_a22_app.haarcascades.haarcascades import detect_objects
from aiortc.contrib.media import MediaPlayer


class VideoSource(SourcesInterface):
    def load_source(self, classifier_id: str, scale_factor: int, min_neighbors: int, min_size: int, show_results: bool = False):
        """
        This function shows a video player where the haar cascade detection is applied on  single frames.  
        The player uses WebRTC to stream the video.

        The parameter description was taken from: 
        https://hackaday.io/project/12384-autofan-automated-control-of-air-flow/log/41956-face-detection-using-a-haar-cascade-classifier


        Parameters
        ----------
        classifier_id : str
            the classifier name. E.g. when you set it to "frontalface_default", the configuration file
            "haarcascade_frontalface_default.xml" will be loaded
        scale_factor : float, optional, by default 1.1
            determines the factor by which the detection window of the classifier is scaled down per detection pass. A factor of 1.1
            corresponds to an increase of 10%. Hence, increasing the scale factor increases performance, as the number of detection
            passes is reduced. However, as a consequence the reliability by which a face is detected is reduced. See:
        min_neighbors : int, optional, by default 4
            determines the minimum number of neighboring facial features that need to be present to indicate the detection of a face by the
            classifier. Decreasing the factor increases the amount of false positive detections. Increasing the factor might lead to missing
            faces in the image. The argument seems to have no influence on the performance of the algorithm. See:
        min_size: int
            determines the minimum size of the detection window in pixels. Increasing the minimum detection window increases performance. 
            However, smaller faces are going to be missed then. In the scope of this project however a relatively big detection window can 
            be used, as the user is sitting directly in front of the camera.
        show_results : bool, optional
            If true we want to display the original images AND the results, by default False
        """
        st.subheader("Video processing using WebRTC (peer2peer)")

        # Callback function that takes an image frame that can
        # be processed
        def callback(frame):
            # convert frame to ndarray
            img = frame.to_ndarray(format="bgr24")

            # actual object detection
            result_img, result_faces = detect_objects(
                img, classifier_id, scale_factor, min_neighbors, min_size)

            return av.VideoFrame.from_ndarray(result_img, format="bgr24")

        rtc_configuration = {  # Add this config
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        }

        def create_player():
            return MediaPlayer("resources/videos/musk.mp4")

        # This will show the video-UI elements in Streamlit
        # Each frame gets sent to the callback method
        webrtc_streamer(key="videoexample",
                        video_frame_callback=callback,
                        rtc_configuration=rtc_configuration,
                        mode=WebRtcMode.RECVONLY,
                        player_factory=create_player,
                        media_stream_constraints={
                            "video": True
                        }
                        )

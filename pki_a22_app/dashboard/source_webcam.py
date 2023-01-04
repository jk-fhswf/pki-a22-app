"""Impementation of a source-type to display a webcam stream and apply the Haar Cascade classifier on it"""

# Core Pkgs

import av
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer

from pki_a22_app.dashboard.sources import SourcesInterface
from pki_a22_app.haarcascades.haarcascades import detect_objects


class WebcamSource(SourcesInterface):
    def load_source(self, classifier_id: str, scale_factor: int, min_neighbors: int,
                    show_results: bool = False) -> None:
        """
        This method shows an UI element to display the stream of a webcam. The Haar Cascade classifier will then be applied to the images
        of the webcam

        Parameters
        ----------
        classifier_id : str
            the classifier name. E.g. when you set it to "frontalface_default", the configuration file
            "haarcascade_frontalface_default.xml" will be loaded
        scale_factor : float, optional, by default 1.1
            determines the factor by which the detection window of the classifier is scaled down per detection pass. A factor of 1.1
            corresponds to an increase of 10%. Hence, increasing the scale factor increases performance, as the number of detection
            passes is reduced. However, as a consequence the reliability by which a face is detected is reduced. See:
            https://hackaday.io/project/12384-autofan-automated-control-of-air-flow/log/41956-face-detection-using-a-haar-cascade-classifier
        min_neighbors : int, optional, by default 4
            determines the minimum number of neighboring facial features that need to be present to indicate the detection of a face by the
            classifier. Decreasing the factor increases the amount of false positive detections. Increasing the factor might lead to missing
            faces in the image. The argument seems to have no influence on the performance of the algorithm. See:
            https://hackaday.io/project/12384-autofan-automated-control-of-air-flow/log/41956-face-detection-using-a-haar-cascade-classifier
        show_results : bool, optional
            If true we want to display the original images AND the results, by default False
        """
        st.subheader("Webcam using WebRTC (peer2peer)")

        def callback(frame):
            # convert frame to ndarray
            img = frame.to_ndarray(format="bgr24")

            # actual object detection
            result_img, result_faces = detect_objects(
                img, classifier_id, scale_factor, min_neighbors)

            return av.VideoFrame.from_ndarray(result_img, format="bgr24")

        # This will show the webcam-UI elements in streamlit
        # Each frame gets sent to the callback method
        rtc_configuration={  # Add this config
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        }
        webrtc_streamer(key="example", video_frame_callback=callback, rtc_configuration=rtc_configuration)

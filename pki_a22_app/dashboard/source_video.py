"""Impementation of a source-type to select a video and apply the Haar Cascade classifier on it"""

# Core Pkgs

import streamlit as st

from pki_a22_app.dashboard.sources import SourcesInterface


class VideoSource(SourcesInterface):
    def load_source(self, classifier_id: str, scale_factor: int, min_neighbors: int, show_results: bool = False):
        """
        This method shows a selectbox to select an existing Videos. The Haar Cascade classifier will then be applied to the Video.

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
        st.subheader("Video using WebRTC (peer2peer)")
        st.write("Not implemented yet...")

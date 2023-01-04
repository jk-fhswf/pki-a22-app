"""Impementation of a source-type to upload an image and apply the Haar Cascade classifier on it"""
# Core Pkgs

import numpy as np
import streamlit as st
from PIL import Image

from pki_a22_app.dashboard.sources import SourcesInterface
from pki_a22_app.haarcascades.haarcascades import detect_objects


class UploadSource(SourcesInterface):
    def load_source(self, classifier_id: str, scale_factor: int, min_neighbors: int, show_results: bool = False):
        """
        This method creates a form to upload an image that can be processed by the haar cascade classifier afterwards.


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
        st.subheader("Upload an image")

        # Show the upload form
        image_file = st.file_uploader(
            "Upload Image", type=['jpg', 'png', 'jpeg'])
        our_image = None

        # If a image was uploaded, display it
        if image_file is not None:
            our_image = Image.open(image_file)
            our_np_image = np.array(our_image.convert('RGB'))
            st.text("Original Image")
            st.image(our_image)
            image_location = st.empty()

        # Show processed image
        if show_results and classifier_id:
            # Actual object detection
            result_img, result_faces = detect_objects(
                our_np_image, classifier_id, scale_factor, min_neighbors)
            image_location.image(result_img)
            st.text("Resulting Image")
            st.success(f"Found {len(result_faces)} Objects")

"""Impementation of a source-type that show multiple images at once"""

# Core Pkgs
from itertools import cycle

import numpy as np
import streamlit as st
from PIL import Image

from pki_a22_app.dashboard.sources import SourcesInterface
from pki_a22_app.haarcascades.haarcascades import detect_objects
from pki_a22_app.utils.file_loader import get_datasets, get_images_of_dataset


class DatasetSource(SourcesInterface):
    """
    Implementation for handling multiple images, also called dataset here

    Methods
    -------
    load_source(classifier_id: str, scale_factor: int, min_neighbors: int, show_results: bool = False)
        Load multiple images and display results
    """

    def load_source(self, classifier_id: str, scale_factor: int, min_neighbors: int, show_results: bool = False):
        """
        This method shows a selectbox to select an existing dataset. A dataset contains multiple images. The datasets are located
        at resource/datasets/. The Haar Cascade classifier will then be applied to all images of the dataset.

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
        st.subheader("Load an existing dataset")

        # Setup dataset selector
        datasets = get_datasets()
        datasets.insert(0, "None")
        dataset_selection = st.selectbox("Dataset", datasets)

        # When a dataset was selected start presenting it
        if dataset_selection and dataset_selection != "None":
            images_in_ds = get_images_of_dataset(dataset_selection)
            
            # Show images in max n columns
            cols = cycle(st.columns(4))
            for idx, filtered_image in enumerate(images_in_ds):
                next(cols).image(str(filtered_image), width=150)

            # We were requested to show the results
            if show_results and dataset_selection:
                images_in_ds = get_images_of_dataset(dataset_selection)
                st.write("Results:")
                cols = cycle(st.columns(4))

                for idx, filtered_image in enumerate(images_in_ds):
                    ds_image = Image.open(filtered_image)
                    ds_np_image = np.array(ds_image.convert('RGB'))
                    # Actual object detection
                    ds_res_image, ds_result_faces = detect_objects(ds_np_image, classifier_id, scale_factor,
                                                                   min_neighbors)
                    col = next(cols)
                    col.image(ds_res_image, width=150, caption=f"{len(ds_result_faces)} objects")

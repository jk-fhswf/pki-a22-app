"""Start a streamlit dashboard showing some haarcascade operations with Opencv"""

# Core Pkgs

import extra_streamlit_components as stx
import streamlit as st
from pki_a22_app.dashboard.source_dataset import DatasetSource
from pki_a22_app.dashboard.source_upload import UploadSource
from pki_a22_app.dashboard.source_video import VideoSource
from pki_a22_app.dashboard.source_webcam import WebcamSource

from pki_a22_app.utils.file_loader import (get_classifiers)


def main():
    """
    Main function that initiates the Streamlit dashboard
    """

    st.title("Haar Cascade Evaluation")
    st.text("Evaluate Haar Cascade classifier")

    # Configure the sources section
    st.subheader("Source")
    chosen_id = stx.tab_bar(data=[
        stx.TabBarItemData(id=1, title="Upload", description=""),
        stx.TabBarItemData(id=2, title="Dataset", description=""),
        stx.TabBarItemData(id=3, title="Video", description=""),
        stx.TabBarItemData(id=4, title="Webcam", description=""),
    ], default=1)

    st.sidebar.image("resources/images/logo-fh-swf-300x93.png")
    st.sidebar.markdown("#")
    
    # Configure the algorithm controls
    classifiers: list = get_classifiers()
    classifier_id = st.sidebar.selectbox("Classifier", classifiers)
    scale_factor = st.sidebar.slider("Scale Factor", 1.0, 2.0, 1.1, 0.1)
    min_neighbors = st.sidebar.slider("Min Neighbors", 1, 20, 5, 1)
    min_size = st.sidebar.slider("Min Size", 10, 150, 30, 5)

    show_results = st.sidebar.button("RUN")

    # Define different sources that render the input and output accordingly
    sources = {
        "1": UploadSource(),
        "2": DatasetSource(),
        "3": VideoSource(),
        "4": WebcamSource()
    }

    # Execute selected source
    sources[chosen_id].load_source(
        classifier_id, scale_factor,  min_neighbors, min_size, show_results)


if __name__ == "__main__":
    main()

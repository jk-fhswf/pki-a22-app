# Core Pkgs
from itertools import cycle
import os
import pathlib

import cv2
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_webrtc import webrtc_streamer

from pki_a22_app.utils.file_loader import get_classifiers, get_datasets, get_images
import av

def detect_objects(np_input_image, classifier_id: str, scale_factor: float=1.1, max_neighbors: int=4):
    classifier = cv2.CascadeClassifier(f'resources/haarcascades/haarcascade_{classifier_id}.xml')

    img = cv2.cvtColor(np_input_image, 1)
    gray = cv2.cvtColor(np_input_image, cv2.COLOR_BGR2GRAY)
    objects = classifier.detectMultiScale(gray, scale_factor, max_neighbors)
    for (x, y, w, h) in objects:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return img, objects


def main():
    st.title("Haar Cascade Evaluation")
    st.text("Evaluate Haar Cascade classifier")

    st.subheader("Source")


    tab_upload, tab_dataset, tab_video, tab_webcam = st.tabs(["Upload", "Dataset", "Video", "Webcam"])
    data = np.random.randn(10, 1)

    tab_upload.subheader("Upload an image")
    image_file = tab_upload.file_uploader(
        "Upload Image", type=['jpg', 'png', 'jpeg'])
    our_image = None
    
    if image_file is not None:
        our_image = Image.open(image_file)
        our_np_image = np.array(our_image.convert('RGB'))
        st.text("Original Image")
        tab_upload.image(our_image)
        imageLocation = st.empty()
    enable_webcam = tab_webcam.checkbox('Enable Webcam')

 

    tab_dataset.subheader("Load an existing dataset")
    #tab_dataset.line_chart(data)
    #tab_dataset.write(data)
    #datasets = ['None'].extend(get_datasets())
    datasets = get_datasets()

    dataset_selection = tab_dataset.selectbox("Dataset", datasets)
    if dataset_selection:
        images_in_ds = get_images(dataset_selection)
        caption = []
        cols = cycle(tab_dataset.columns(4)) 
        for idx, filteredImage in enumerate(images_in_ds):
            next(cols).image(str(filteredImage), width=150, caption=idx)
    


    classifiers = get_classifiers()
    print(type(classifiers))
    classifier_selection = st.sidebar.selectbox("Classifier", classifiers)
    scale_factor = st.sidebar.slider('Scale Factor', 1.0, 2.0, 1.1, 0.1)
    max_neighbors = st.sidebar.slider('Max Neighbors', 1, 10, 5, 1)
    st.write(f'Values: {scale_factor} {max_neighbors}')
    if st.sidebar.button("RUN"):
        if our_image:
            result_img, result_faces = detect_objects(our_np_image, classifier_selection, scale_factor, max_neighbors)
            imageLocation.image(result_img)
            st.text("Resulting Image")
            st.success("Found {} Objects".format(len(result_faces)))
        if classifier_selection:
            images_in_ds = get_images(dataset_selection)
            caption = []
            cols = cycle(tab_dataset.columns(4)) 
            for idx, filteredImage in enumerate(images_in_ds):
                ds_image = Image.open(filteredImage)
                ds_np_image = np.array(ds_image.convert('RGB'))
                ds_res_image, ds_result_faces = detect_objects(ds_np_image, classifier_selection, scale_factor, max_neighbors)

                next(cols).image(ds_res_image, width=150, caption=idx)
                
    def callback(frame):
        img = frame.to_ndarray(format="bgr24")
        
        img = cv2.cvtColor(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        classifier = cv2.CascadeClassifier(f'resources/haarcascades/haarcascade_{classifier_selection}.xml')
        objects = classifier.detectMultiScale(gray, scale_factor, max_neighbors)
        for (x, y, w, h) in objects:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)        
        
        return av.VideoFrame.from_ndarray(img, format="bgr24")
    
    if enable_webcam:
        webrtc_streamer(key="example", video_frame_callback=callback)
    


if __name__ == '__main__':
    main()

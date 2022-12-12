import glob
import os
import pathlib

def get_classifiers():
    classifier_files = os.listdir(os.getcwd() + "/resources/haarcascades/")
    classifiers = [item.replace("haarcascade_", "") for item in classifier_files]
    classifiers = [item.replace(".xml", "") for item in classifiers]
    classifiers.sort()
    return classifiers

def get_datasets():
    ds = os.listdir(os.getcwd() + "/resources/datasets/")
    ds.sort()
    return ds

def get_images(ds):
    img_list = pathlib.Path(f"resources/datasets/{ds}").glob('*.*')
    img_list = [str(item) for item in img_list ]
    return list(img_list)
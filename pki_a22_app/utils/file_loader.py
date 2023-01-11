"""This modules contains helper methods to get information from local file system"""
import os
import pathlib
from typing import List


def get_classifiers() -> List[str]:
    """
    Reads all files in /resources/haarcascades/ and returns only the actual classifier
    name without "haarcascade_" and ".xml". "E.g. haarcascade_frontalface_default.xml"
    gets to "haarcascade_frontalface_default".

    Returns
    -------
    List[str]
        List of found classifiers
    """
    classifier_files = os.listdir(os.getcwd() + "/resources/haarcascades/")
    classifiers = [item.replace("haarcascade_", "")
                   for item in classifier_files]
    classifiers = [item.replace(".xml", "") for item in classifiers]
    classifiers.sort()
    return classifiers


def get_datasets() -> List[str]:
    """
    Returns the folders found under /resources/datasets/

    Returns
    -------
    List[str]
        List of available dataset
    """
    datasets = os.listdir(os.getcwd() + "/resources/datasets/")
    datasets = [item for item in datasets if not item.startswith(".")]
    datasets.sort()
    return datasets


def get_images_of_dataset(dataset_name: str) -> List[str]:
    """
    Returns the images contined in a dataset

    Parameters
    ----------
    dataset_name : str
        Name of the dataset (folder)

    Returns
    -------
    List[str]
        List of found images
    """
    extensions = ['.jpg', '.png', '.jpeg']
    img_list = [x for x in pathlib.Path(f"resources/datasets/{dataset_name}").iterdir() if x.suffix.lower() in extensions]
    img_list = [str(item) for item in img_list]
    return list(img_list)

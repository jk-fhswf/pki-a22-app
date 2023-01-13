"""This module contains haar cascade core functionality"""

import cv2
from cv2 import Mat
import numpy.typing as npt


def detect_objects(np_input_image: npt.ArrayLike, classifier_id: str, scale_factor: float = 1.1, min_neighbors: int = 4, min_size: int = 10) -> Mat:
    """
    Detects objects in an image using Haar Cascades classifiers. It can usa a preset of trained classifiers in resources/haarcascades/*.
    The found objects get highlighted by a rectangle around it.

    The parameter description was taken from: 
    https://hackaday.io/project/12384-autofan-automated-control-of-air-flow/log/41956-face-detection-using-a-haar-cascade-classifier


    Parameters
    ----------
    np_input_image : npt.ArrayLike
        The input image
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

    Returns
    -------
    cv2.Mat
        The image in Mat representation
    list
        A list of found objects in the image
    """

    classifier = cv2.CascadeClassifier(
        f"resources/haarcascades/haarcascade_{classifier_id}.xml")

    img = cv2.cvtColor(np_input_image, 1)
    gray = cv2.cvtColor(np_input_image, cv2.COLOR_BGR2GRAY)
    objects = classifier.detectMultiScale(
        gray, scaleFactor=scale_factor, minNeighbors=min_neighbors, minSize=(min_size, min_size))
    # pylint: disable=invalid-name
    for (x, y, w, h) in objects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (72, 209, 204), 4)
    return img, objects

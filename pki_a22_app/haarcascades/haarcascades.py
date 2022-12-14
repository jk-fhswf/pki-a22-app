"""This module contains haar cascade core functionality"""

import cv2
from cv2 import Mat
import numpy.typing as npt

def detect_objects(np_input_image: npt.ArrayLike, classifier_id: str, scale_factor: float = 1.1, min_neighbors: int = 4) -> Mat:
    """
    Detects objects in an image using Haar Cascades classifiers. It can usa a preset of trained classifiers in resources/haarcascades/*.
    The found objects get highlighted by a rectangle around it.


    Parameters
    ----------
    np_input_image : npt.ArrayLike
        The input impage
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

    Returns
    -------
    cv2.Mat
        The image in Mat representation
    list
        A list of found objects in the image
    """

    classifier = cv2.CascadeClassifier(
        f'resources/haarcascades/haarcascade_{classifier_id}.xml')

    img = cv2.cvtColor(np_input_image, 1)
    gray = cv2.cvtColor(np_input_image, cv2.COLOR_BGR2GRAY)
    objects = classifier.detectMultiScale(gray, scale_factor, min_neighbors)
    # pylint: disable=invalid-name
    for (x, y, w, h) in objects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img, objects


def show() -> None:
    """
    Dummy function that gets called initally
    TODO: implement tKinter app
    """
    pass

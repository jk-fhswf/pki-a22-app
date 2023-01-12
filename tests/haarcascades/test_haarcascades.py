from PIL import Image
from numpy import asarray

from pki_a22_app.haarcascades.haarcascades import detect_objects


def test_detect_objects():
    image = Image.open('resources/datasets/XFiles/img4.jpg')
    image_arr = asarray(image)
    img, found_objects = detect_objects(
        np_input_image=image_arr, classifier_id="eye", min_neighbors=5, scale_factor=1.1)
    assert img is not None, "Image should be not None"
    assert len(found_objects) == 4, "There should be 4 eyes detected"

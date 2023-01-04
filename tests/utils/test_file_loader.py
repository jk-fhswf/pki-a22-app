import glob

from pki_a22_app.utils.file_loader import get_classifiers, get_images_of_dataset



def test_get_classifiers():
    classifiers = get_classifiers()
    assert len(classifiers) > 0

def test_get_images():
    res = get_images_of_dataset("xfiles")
    assert len(res) > 0
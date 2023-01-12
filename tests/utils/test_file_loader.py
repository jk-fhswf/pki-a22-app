from pki_a22_app.utils.file_loader import get_classifiers, get_datasets, get_images_of_dataset


def test_get_classifiers():
    classifiers = get_classifiers()
    assert len(classifiers) > 0, "No classifiers found"

def test_get_images():
    res = get_images_of_dataset("XFiles")
    assert len(res) > 0, "No images in dataset found"
    
def test_get_datasets():
    res = get_datasets()
    assert len(res) > 0, "No datasets found"
    

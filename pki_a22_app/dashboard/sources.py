"""
Contains an interface definition to use different source-types
in the Streamlit dashboard
"""
import abc


class SourcesInterface(metaclass=abc.ABCMeta):
    """
    Interface for handling different input source types

    Methods
    -------
    load_source(classifier_id: str, scale_factor: int, min_neighbors: int, show_results: bool = False)
        Load the sources and outputs with respect to the given parameters
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        """
        Ensures that needed methods are implemented in your derivatives

        Parameters
        ----------
        subclass : Any
            subclass that was created

        Returns 
        -------
        Bool
            True if it is a valid subclass
        """
        return (hasattr(subclass, 'load_source') and
                callable(subclass.load_source) or
                NotImplemented)


    @abc.abstractmethod
    def load_source(self, classifier_id: str, scale_factor: int, min_neighbors: int, min_size: int, show_results: bool = False):
        """
        This method handles the display of different Streamlit-UI elements. Implement these in your
        concrete derivatives

        The parameter description was taken from: 
        https://hackaday.io/project/12384-autofan-automated-control-of-air-flow/log/41956-face-detection-using-a-haar-cascade-classifier

        Parameters
        ----------
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
        show_results : bool, optional
            If true we want to display the original images AND the results, by default False

        Raises
        ------
        NotImplementedError
            Error that gets thrown if you do not implement this function
        """
        raise NotImplementedError

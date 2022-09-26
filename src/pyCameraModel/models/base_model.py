from abc import ABC, abstractclassmethod
import numpy as np


class BaseModel(ABC):

    N = 4

    def __init__(
            self,
            intrinsic_params: np.ndarray = np.zeros(4),
            img_wh: np.ndarray = np.zeros(2),
    ) -> None:
        self.intrinsic_params = intrinsic_params

    @property
    @abstractclassmethod
    def D(cls):
        """number of distortion parameters"""
        raise NotImplementedError

    @abstractclassmethod
    def project(cls, intrinsic, obj_pts):
        """project obj points to img points"""
        pass

    # @abstractclassmethod
    # def unproject(cls, intrinsic, obj_pts):
    #     """unproject img points to z=1 obj points"""
    #     pass

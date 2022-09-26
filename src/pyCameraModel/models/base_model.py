from abc import ABC, abstractclassmethod


class BaseModel(ABC):

    N = 4

    def __init__(self) -> None:
        super().__init__()

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

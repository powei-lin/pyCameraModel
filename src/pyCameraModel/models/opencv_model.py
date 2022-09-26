from .base_model import BaseModel


class OpenCVModel(BaseModel):
    D = 2

    def project(cls, intrinsic, obj_pts):
        """project obj points to img points"""
        print(cls, intrinsic, obj_pts)

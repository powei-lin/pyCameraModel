from .base_model import BaseModel


class UCM(BaseModel):
    D = 1

    def project(cls, intrinsic, obj_pts):
        """project obj points to img points"""
        # print(cls, intrinsic, obj_pts)
        pass

import pytest
from pyCameraModel.models import UCM, OpenCVModel


def test0():
    b = UCM()
    UCM.D != 5
    UCM().project(0, 0)


def test_project():
    m = OpenCVModel()
    print(m.intrinsic_params)
    # intrinsic = np.eye(3, 3)
    # intrinsic[0, 0] = 1000.0
    # intrinsic[1, 1] = 1000.0
    # intrinsic[0, 2] = 960.0
    # intrinsic[1, 2] = 540.0

    # distortion = np.random.random((1, 5))
    # distortion[0, 2] = 0
    # distortion[0, 3] = 0
    # print(distortion)
    # obj_pts = np.random.random((10, 3)) + [0, 0, 1]
    # print(obj_pts)

    # img_pts, _ = cv2.projectPoints(obj_pts, np.zeros(3), np.zeros(3), intrinsic, distortion)
    # print(img_pts)
    m.project(1, 1)

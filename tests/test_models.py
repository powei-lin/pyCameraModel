import pytest
from pyCameraModel.models.ucm import UCM

def test0():
  b = UCM()
  assert b.D != 5
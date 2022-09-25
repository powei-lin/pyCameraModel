from abc import ABC, abstractclassmethod

class BaseModel(ABC):

  N = 4

  def __init__(self) -> None:
    super().__init__()

  @property
  @abstractclassmethod
  def D(cls):
    """ number of distortion parameters"""
    raise NotImplementedError

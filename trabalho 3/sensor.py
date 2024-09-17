from abc import abstractclassmethod
from abc import ABC

class Sensor(ABC):
    def __init__(self, id, num_serie): 
        self.id = id 
        self.num_serie = num_serie 

    @abstractclassmethod
    def criarsensor(self):
        pass
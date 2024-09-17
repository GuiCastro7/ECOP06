from sensor import Sensor

class Atuadores(Sensor):
    def __init__(self, id, num_serie, pointTemp, pointPress):
        super().__init__(id, num_serie)
        self.pointTemp = pointTemp
        self.pointPress = pointPress

    @property
    def pointTemp (self):
        return self._pointTemp
    
    @pointTemp.setter
    def pointTemp (self, pointTemp):
        self._pointTemp = pointTemp

    @property
    def pointPress (self):
        return self._pointPress
    
    @pointPress.setter
    def pointPress (self, pointPress):
        self._pointPress = pointPress
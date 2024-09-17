from sensor import Sensor

class Temperatura(Sensor):
    def __init__(self, id, num_serie, temp):
        super().__init__(id, num_serie)
        self.temp = temp
      

    @property
    def temp (self):
        return self._temp
    
    @temp.setter
    def temp (self, temp):
        self._temp = temp
        

    def criarsensor(self):
        print("Sensor temperatura foi criado. id: {} e num_serie: {}.".format(self.id, self.num_serie))
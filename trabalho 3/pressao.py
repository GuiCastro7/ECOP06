from sensor import Sensor

class Pressao(Sensor):
    def __init__(self, id, num_serie, press):
        super().__init__(id, num_serie)
        self.press = press


    @property
    def press (self):
        return self._press
    
    @press.setter
    def press (self, press):
        self._press = press
        
    def criarsensor(self):
        print("Sensor pressão foi criado. id: {} e num_serie: {}.".format(self.id, self.num_serie))    
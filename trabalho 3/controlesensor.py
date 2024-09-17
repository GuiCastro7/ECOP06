import time
from temperatura import Temperatura
from pressao import Pressao
from atuadores import Atuadores
from arcondicionado import ArCondicionado
from regulador import Regulador
from excecoes import ForaLimiteMenor, ForaLimiteMaior

class ControleSensor:
    def __init__(self):
        self.sensores = []
        self.arcondicionado = None
        self.regulador = None

    def adicionar_sensor(self, sensor):
        if isinstance(sensor, Temperatura):
            if not self.arcondicionado:
                self.arcondicionado = ArCondicionado(id=f"AC_{sensor.id}", qtdResf=5)
        elif isinstance(sensor, Pressao):
            if not self.regulador:
                self.regulador = Regulador(id=f"Reg_{sensor.id}", qtdPres=10)
        self.sensores.append(sensor)

    def verificar_temp(self):
        for sensor in self.sensores:
            if isinstance(sensor, Temperatura):
                temp = sensor.get_temperatura()
                pointTemp = self.ar_condicionado.qtdResf if self.ar_condicionado else 0

                if temp < pointTemp - 5:
                    raise ForaLimiteMenor("A temperatura está baixa, o ar será desligado")
                elif temp > pointTemp + 5:
                    raise ForaLimiteMaior("A temperatura está alta, o ar será ligado")

    def ajustar_temp(self):
        for sensor in self.sensores:
            if isinstance(sensor, Temperatura):
                temp = sensor.get_temperatura()
                pointTemp = self.ar_condicionado.qtdResf if self.ar_condicionado else 0

                if temp < pointTemp - 5:
                    self.desliga_ar()
                elif temp > pointTemp + 5:
                    self.liga_ar()

    def verificar_pres(self):
        for sensor in self.sensores:
            if isinstance(sensor, Pressao):
                pres = sensor.get_pressao()
                pointPres = self.regulador.qtdPres if self.regulador else 0

                if pres < pointPres - 10:
                    raise ForaLimiteMenor("A pressão está baixa, o regulador será ligado")
                elif pres > pointPres + 10:
                    raise ForaLimiteMaior("A pressão está alta, o regulador será desligado")

    def ajustar_pres(self):
        for sensor in self.sensores:
            if isinstance(sensor, Pressao):
                pres = sensor.get_pressao()
                pointPres = self.regulador.qtdPres if self.regulador else 0

                if pres < pointPres - 10:
                    self.liga_reg()
                elif pres > pointPres + 10:
                    self.desliga_reg()

    def liga_ar(self):
        if self.ar_condicionado:
            self.ar_condicionado.ligar()

    def desliga_ar(self):
        if self.ar_condicionado:
            self.ar_condicionado.desligar()

    def liga_reg(self):
        if self.regulador:
            self.regulador.ligar()

    def desliga_reg(self):
        if self.regulador:
            self.regulador.desligar()

    def update_temp(self):
        for sensor in self.sensores:
            if isinstance(sensor, Temperatura):
                if self.ar_condicionado and self.ar_condicionado.esta_ligado():
                    sensor.set_temperatura(sensor.get_temperatura() - self.ar_condicionado.qtdResf)
                else:
                    sensor.set_temperatura(sensor.get_temperatura() + self.ar_condicionado.qtdResf)

    def update_pres(self):
        for sensor in self.sensores:
            if isinstance(sensor, Pressao):
                if self.regulador and self.regulador.esta_ligado():
                    sensor.set_pressao(sensor.get_pressao() + self.regulador.qtdPres)
                else:
                    sensor.set_pressao(sensor.get_pressao() - self.regulador.qtdPres)

    def monitorar(self):
        while True:
            try:
                self.verificar_temp()
                self.ajustar_temp()
            except (ForaLimiteMenor, ForaLimiteMaior) as e:
                print(e)

            try:
                self.verificar_pres()
                self.ajustar_pres()
            except (ForaLimiteMenor, ForaLimiteMaior) as e:
                print(e)

            self.update_temp()
            self.update_pres()

            for sensor in self.sensores:
                print(f"Sensor ID: {sensor.id}, Tipo: {'Temperatura' if isinstance(sensor, Temperatura) else 'Pressão'}, Valor: {sensor.obter_dados()}")

            time.sleep(5)

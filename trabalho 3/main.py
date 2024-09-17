from controlesensor import ControleSensor
from temperatura import Temperatura
from pressao import Pressao
import time
from excecoes import foraLimiteMenor, foraLimiteMaior

def main():
    controle_sensor = ControleSensor()

    # Criando 3 sensores de cada tipo
    for i in range(3):
        temp_sensor = Temperatura(id=f"T_{i}", numero_serie=f"T_S{i}", temperatura=20 + i)
        pres_sensor = Pressao(id=f"P_{i}", numero_serie=f"P_S{i}", pressao=1000 + i * 10)
        controle_sensor.adicionar_sensor(temp_sensor)
        controle_sensor.adicionar_sensor(pres_sensor)

    # Loop infinito para monitorar os sensores
    while True:
        try:
            controle_sensor.verificar_temp()
            controle_sensor.ajustar_temp()
        except (foraLimiteMenor, foraLimiteMaior) as e:
            print(e)

        try:
            controle_sensor.verificar_pres()
            controle_sensor.ajustar_pres()
        except (foraLimiteMenor, foraLimiteMaior) as e:
            print(e)

        controle_sensor.update_temp()
        controle_sensor.update_pres()

        for sensor in controle_sensor.sensores:
            print(f"Sensor ID: {sensor.id}, Tipo: {'Temperatura' if isinstance(sensor, Temperatura) else 'Pressão'}, Valor: {sensor.obter_dados()}")

        time.sleep(5)

if __name__ == "__main__":
    main()


#passar para o controller os dados abaixo
senstemp1 = Temperatura("1232", "50", 20)
senspress1 = Pressao("1232", "50", 1)
senstemp2 = Temperatura("9876", "40", 25)
senspress2 = Pressao("9876", "40", 1,2)
senstemp3 = Temperatura("8024", "30", 30)
senspress3 = Pressao("8024", "30", 1,5)

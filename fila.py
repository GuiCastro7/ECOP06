import random
import time

class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # Nome da pessoa
        self.tempo_chegada = random.randint(3, 5)  # Tempo de chegada (entre 3 e 5 segundos)
        self.tempo_espera = self.tempo_chegada  # Inicializa o tempo de espera com o tempo de chegada

    def __str__(self):
        return self.nome


class Fila:
    def __init__(self):
        self.pessoas = []  # Agora usamos uma lista para representar a fila
        self.adciona_pessoas = random.randint(3, 5) # Tempo de entrar na fila (entre 3 e 5 segundos)

    def push(self, pessoa):
        """Adiciona uma pessoa no fim da fila."""
        self.pessoas.append(pessoa)
        self.adciona_pessoas = random.randint(3, 5) # Tempo de entrar na fila (entre 3 e 5 segundos)

    def pop(self):
        """Remove e retorna a pessoa do início da fila."""
        if self.esta_vazia():
                return None
        return self.pessoas.pop(0)  # Remove a pessoa do início da fila
    
    

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.pessoas) == 0


class Caixa:
    def __init__(self, matricula):
        self.matricula = matricula
        self.pessoa_atendendo = None
        self.tempo_atendimento = 0

    def iniciar_atendimento(self, pessoa):
        """Inicia o atendimento de uma pessoa no caixa."""
        self.pessoa_atendendo = pessoa
        self.tempo_atendimento = random.randint(4, 7)  # Tempo de atendimento aleatório (entre 4 e 7 segundos)
        print(f"\n{pessoa} iniciou o atendimento no Caixa {self.matricula}.")

    def atender(self):
        """Simula o atendimento da pessoa."""
        if self.pessoa_atendendo:
            if self.tempo_atendimento > 0:
                self.tempo_atendimento -= 1
                return False  # Atendimento ainda em progresso
            else:
                print(f"{self.pessoa_atendendo} terminou o atendimento no Caixa {self.matricula}.")
                self.pessoa_atendendo = None
                return True  # Atendimento finalizado
        return False


# Função principal
def main():
    # Inicializando fila e caixa
    fila = Fila()
    caixa = Caixa(1)

    contador_pessoas = 1
    tempo_atual = 0  # Controla o tempo atual (em segundos)
    
    # Simulando o atendimento
    while True:
        tempo_atual += 1


        
        # Adiciona uma pessoa à fila a cada 3 segundos (tempo de chegada)
        if fila.adciona_pessoas == 0:  # Limita a 10 segundos para simulação
            pessoa = Pessoa(f"Pessoa {contador_pessoas}")
            print(f"{pessoa} entrou na fila.")
            fila.push(pessoa)
            contador_pessoas += 1
        else:
            fila.adciona_pessoas = fila.adciona_pessoas - 1


        # Verificar se o caixa pode iniciar atendimento
        if caixa.pessoa_atendendo is None and not fila.esta_vazia():
            pessoa_para_atender = fila.pop()
            caixa.iniciar_atendimento(pessoa_para_atender)

        # Verificando atendimento
        if caixa.atender():
            print("Atendimento finalizado. Próximo por favor.")

        time.sleep(1)  # Atraso de 1 segundo

if __name__ == "__main__":
    main()

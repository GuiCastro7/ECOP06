from abc import ABC

# Classe abstrata Pessoa
class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

# Classe Hóspede (concreta)
class Hospede(Pessoa):
    def __init__(self, nome, cpf, codigo_reserva, data_reserva, quarto, funcionario, valor_total):
        super().__init__(nome, cpf)
        self.reserva = Reserva(nome, codigo_reserva, data_reserva, quarto, funcionario, valor_total)


# Classe Funcionario (concreta)
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf)
        self.salario = salario

# Classe Reserva (concreta)
class Reserva:
    def __init__(self, nome, codigo_reserva, data_reserva, quarto, funcionario, valor_total):
        self.nome = nome
        self.codigo_reserva = codigo_reserva
        self.data_reserva = data_reserva
        self.quarto = quarto
        self.funcionario = funcionario
        self.valor_total = valor_total

# Classe Quarto (concreta)
class Quarto:
    def __init__(self, tipo_quarto, numero_quarto, valor):
        self.tipo_quarto = tipo_quarto
        self.numero_quarto = numero_quarto
        self.valor = valor

# Classe ExcecaoReserva
class ExcecaoReserva(Exception):
    pass

# Classe ControleReserva (concreta)
class ControleReserva:
    def __init__(self):
        self.hospedes = []
        self.reservas = []

    def verifica_reserva(self, numero_quarto, data_reserva):
        for reserva in self.reservas:
            if reserva.quarto.numero_quarto == numero_quarto and reserva.data_reserva == data_reserva:
                raise ExcecaoReserva("O quarto está reservado na data selecionada.")

    def cria_reservas(self, nome, cpf_hospede, codigo_reserva, numero_quarto, data_reserva, funcionario):
        quarto_selecionado = next((quarto for quarto in quartos if quarto.numero_quarto == numero_quarto), None)
        if not quarto_selecionado:
            print("Quarto não encontrado.")
            return
        
        self.verifica_reserva(numero_quarto, data_reserva)
        valor_total = quarto_selecionado.valor
        novo_hospede = Hospede(nome, cpf_hospede, codigo_reserva, data_reserva, quarto_selecionado, funcionario, valor_total)
        self.hospedes.append(novo_hospede)
        self.reservas.append(novo_hospede.reserva)

    def imprime_reservas(self):
        for reserva in self.reservas:
            print(f'Hóspede: {reserva.nome}, Data: {reserva.data_reserva.strftime("%d/%m/%Y")}, Quarto: {reserva.quarto.tipo_quarto} {reserva.quarto.numero_quarto}, Funcionário: {reserva.funcionario.nome} {reserva.funcionario.cpf}, Valor: {reserva.valor_total}')

# Criando a lista de quartos
quartos = [] 
quartos.append(Quarto("Simples, num", 1, 50))
quartos.append(Quarto("Simples, num", 2, 50))
quartos.append(Quarto("Simples, num", 3, 50))
quartos.append(Quarto("Duplo, num", 4, 100))
quartos.append(Quarto("Duplo, num", 5, 100))
quartos.append(Quarto("Luxo, num", 6, 200))


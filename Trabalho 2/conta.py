from abc import ABC, abstractmethod



class Conta(ABC): 
    def __init__(self, numero, agencia, cliente):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0.0
        self.historico = []
        
    @abstractmethod
    def cria_conta(self):
        pass

    @abstractmethod
    def saque(self, valor):
        pass

    @abstractmethod
    def deposito(self, valor):
        pass

    @abstractmethod
    def extrato(self):
        pass
        
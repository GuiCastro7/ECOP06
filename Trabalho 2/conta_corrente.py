from conta import Conta

class Conta_Corrente(Conta):
    def __init__(self, numero, agencia, cliente,):
        super().__init__(numero, agencia, cliente)
        self.historico.append("Conta criada com saldo inicial de R$0.00")

    def cria_conta(self):
        return f"Conta Corrente criada: {self.numero}, Agência: {self.agencia}, Cliente: {self.cliente.nome}"

    def saque(self, valor):
        if valor <= 0:
            mensagem = "Nenhum valor fornecido para saque."
        elif valor > self.saldo:
            mensagem = f"Saque: R${valor:.2f}. \nSaldo insuficiente para saque.\nOperação não realizada."
        else:
            self.saldo -= valor
            mensagem = f"Saque: R${valor:.2f}. \nOperação realizada com sucesso\nSaldo atual: R${self.saldo:.2f}"
        self.historico.append(mensagem if valor > 0 else "Saque não registrado.\nOperação não realizada.") 


    def deposito(self, valor):
        if valor <= 0:
            mensagem = "Nenhum valor fornecido para depósito."
        else:
            self.saldo += valor
            mensagem = f"Depósito: R${valor:.2f}."
        self.historico.append(mensagem if valor > 0 else "Depósito não registrado.")

    def extrato(self):
        extrato = (
            f"\nConta Corrente: {self.numero} - Agência: {self.agencia}\n" 
            f"Saldo Atual: R${self.saldo:.2f}\n" 
            f"Histórico de Transações:\n"
        )
        extrato += "\n".join(f"- {transacao}" for transacao in self.historico)
        return extrato
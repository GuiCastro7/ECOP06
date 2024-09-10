from conta_corrente import Conta_Corrente 


class Conta_Poupanca(Conta_Corrente):
    def __init__(self, número, agência, cliente, taxa_juros):
        super().__init__(número, agência, cliente)
        self.taxa_juros = taxa_juros

    def cria_conta(self):
        return (f"Conta Poupança {self.numero}, Agência: {self.agencia}, Cliente: {self.cliente.nome}, Taxa de Juros: {self.taxa_juros}%")

    def aplicar_juros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros
        self.historico.append(f"Aplicação de Juros: {juros:.2f}")

    def deposito(self, valor):
        if valor <= 0:
            mensagem = "Nenhum valor fornecido para depósito."
        else:
            valor_com_juros = valor * (1 + self.taxa_juros / 100)
            self.saldo += valor_com_juros
            mensagem = f"Depósito: R${valor:.2f}. Valor com juros aplicado: R${valor_com_juros:.2f}."
        self.historico.append(mensagem if valor > 0 else "Depósito não registrado.")

    def saque(self, valor):
        if valor <= 0:
            mensagem = "Nenhum valor fornecido para saque."
        elif valor > self.saldo:
            mensagem = f"Saque solicitado: R${valor:.2f}. \nO valor do saque deve ser igual ao saldo atual de R${self.saldo:.2f}.\nOperação não realizada."
        else:
            self.saldo -= valor
            mensagem = f"Saque: R${valor:.2f}. \nOperação realizada com sucesso\nSaldo atual: R${self.saldo:.2f}"
            self.historico.append(mensagem if valor > 0 else "Saque não registrado.\nOperação não realizada.")
   

    def extrato(self):
        extrato = (
            f"\nConta Poupança: {self.numero} - Agência: {self.agencia}\n" 
            f"Saldo Atual: R${self.saldo:.2f}\n" 
            f"Histórico de Transações:\n"
        )
        extrato += "\n".join(f"- {transacao}" for transacao in self.historico)
        return extrato

    


    

from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, num_contrato):
        super().__init__(nome, cpf)
        self.num_contrato = num_contrato
    
    def cria_pessoa(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Contrato: {self.num_contrato}"
        
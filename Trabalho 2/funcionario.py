from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, num_matricula):
        super().__init__(nome, cpf)
        self.num_matricula = num_matricula

    def cria_pessoa(self):
        return f"Funcionário {self.nome}, CPF: {self.cpf}, Matrícula: {self.num_matricula}"    
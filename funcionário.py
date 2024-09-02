from pesssoa import Pessoa #type:ignore

class Funcionario(Pessoa):
    def __init__(self, cpf, cadastro, nome, curso, disciplinas, disciplinas_disponiveis, instituto, salario, funcao):
        super().__init__(nome, cpf, curso, disciplinas, disciplinas_disponiveis, salario)
        self.cadastro = cadastro
        self.funcao = funcao
        self.instituto = instituto

    def define_bonus(self):
        return super().define_bonus() * 1.07
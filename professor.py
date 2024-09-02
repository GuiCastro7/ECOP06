from pessoa import Pessoa #type: ignore

class Professor(Pessoa):
    def __init__(self, cpf, siape, nome, curso, disciplinas, disciplinas_disponiveis, salario):
        super().__init__(nome, cpf, curso, disciplinas, disciplinas_disponiveis, salario)
        self.siape = siape

    def define_bonus(self):
        return super().define_bonus() * 1.15
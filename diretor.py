from pessoa import Pessoa #type: ignore

class Diretor(Pessoa):
    def __init__(self, cpf, siape, nome, curso, disciplinas, disciplinas_disponiveis, instituto, salario):
        super().__init__(nome, cpf, curso, disciplinas, disciplinas_disponiveis, salario)
        self.siape = siape
        self.instituto = instituto
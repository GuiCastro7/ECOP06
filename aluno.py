from pessoa import Pessoa #type: ignore

class Aluno(Pessoa):
    def __init__(self, cpf, matricula, nome, curso, disciplinas, disciplinas_disponiveis):
        super().__init__(nome, cpf, curso, disciplinas, disciplinas_disponiveis)
        self.matricula = matricula
        #self.historico = Historico(self)

    def  define_bonus(self):
        return self.salario

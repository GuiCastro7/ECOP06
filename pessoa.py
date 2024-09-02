class Pessoa():
    def __init__(self, nome, cpf, curso, disciplinas, disciplinas_disponiveis, salario=0):
        self.nome = nome
        self.cpf = cpf
        self.curso = curso
        self.salario = salario
        self.disciplinas = []

        for disc in disciplinas:
            for disc_disp in disciplinas_disponiveis:
                if disc == disc_disp.nome:
                    self.disciplinas.append(disc_disp)


    
    
    def define_bonus(self):
        self.salario + 2000
        return
    
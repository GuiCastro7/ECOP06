class Aluno:  

    def __init__(self, matricula, nome, curso, disciplinas, disciplinas_disponiveis):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
    
        self.disciplinas = []
        for disc in disciplinas:
            for disc_disp in disciplinas_disponiveis:
                if disc == disc_disp.nome:
                    self.disciplinas.append(disc_disp)
                    print("Aluno {} inserido com sucesso em {}".format(self.nome,disc))
                    break
                else:
                    print("Aluno {} não pode se matricular na disciplina {}".format(self.nome,disc))

    def insere_disciplina(self, disciplina, disciplinas_disponiveis):
        if disciplina in disciplinas_disponiveis:
            self.disciplina.append(disciplina)
            return "Aluno matriculado"
        else:
            return "Aluno não matriculado"
        
    def imprime_aluno(self):
        print("Nome: {}".format(self.nome))
        print("Professor: {}".format(self.matricula))
        print("Carga horaria: {}".format(self.curso))
        for x in range (len(self.disciplinas)):

            print(self.disciplinas(x).nome)
             
   

        
    
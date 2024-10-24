class Aluno:

    def __init__(self, nome, matricula, idade, nroDisciplinas):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.nroDisciplinas = nroDisciplinas
        self.prox = None
        self.ant = None

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.qtdAlunos = 0
        self.prox = None
        self.ant = None
        self.inicioAluno = None

class Lista:
    def __init__(self):
       self.universidades = None 

    def insere_universidade(self, nome):

        if self.busca_universidade(nome):
            print("Universidade já cadastrada.")
            return
        
        nova_uni = Universidade(nome)

        if  self.universidades == None:
                self.universidades = nova_uni

        else:
            atual = self.universidades
            ant = None
            
        #Insere faculdade em ordem alfabetica
            while atual and atual.nome < nome:
                    ant = atual
                    atual = atual.prox

            if ant == None:
                nova_uni.prox = self.universidades
                self.universidades.ant = nova_uni
                self.universidades = nova_uni
            else:
                ant.prox = nova_uni
                nova_uni.ant = ant
                nova_uni.prox = atual
                if atual:
                    atual.ant = nova_uni
                    
        nova_uni = nome
        print("Universidade {} inserida com sucesso.".format(nome))

    def insere_aluno(self, nome_uni, nome, matricula, idade, nro_disciplinas):
        universidade = self.busca_universidade(nome_uni)
        if universidade == None:
            print("Universidade não encontrada.")

            opcao = input("Deseja tentar outra universidade? (1 para sim, qualquer outra tecla para não): ")
            if opcao == "1":
                nome_uni = input("Informe o nome da nova universidade: ")
                self.insere_aluno(nome_uni, nome, matricula, idade, nro_disciplinas)
            return
        
        atual_aluno = universidade.inicioAluno
        while atual_aluno:
            if atual_aluno.matricula == matricula:
                print(("Aluno com matrícula {:02d} já existe na universidade {}.".format(matricula, nome_uni)))
                return
            atual_aluno = atual_aluno.prox

        novo_aluno = Aluno(nome, matricula, idade, nro_disciplinas)

        # Inserir aluno por ordem crescente de matrícula
        if universidade.inicioAluno == None:
            universidade.inicioAluno = novo_aluno
        else:
            atual = universidade.inicioAluno
            anterior = None

            while atual and atual.matricula < matricula:
                anterior = atual
                atual = atual.prox

            if anterior == None:
                novo_aluno.prox = universidade.inicioAluno
                universidade.inicioAluno.ant = novo_aluno
                universidade.inicioAluno = novo_aluno
            else:
                anterior.prox = novo_aluno
                novo_aluno.ant = anterior
                novo_aluno.prox = atual
                if atual:
                    atual.ant = novo_aluno

        universidade.qtdAlunos += 1
        print("Aluno {} inserido com sucesso na universidade {}.".format(nome, nome_uni))
       

    def busca_universidade(self, nome):
        atual = self.universidades
        while atual:
            if atual.nome == nome:
                print("Universidade {} encontrada com {} alunos.".format(atual.nome, atual.qtdAlunos))   

                aluno_atual = atual.inicioAluno
                if aluno_atual == None:
                    print("Nenhum aluno matriculado.")
                else:
                    print("Alunos matriculados:")
                    while aluno_atual:
                        print("Nome: {}, Matrícula: {:02d}".format(aluno_atual.nome,aluno_atual.matricula))
                        aluno_atual = aluno_atual.prox         
                return atual
            atual = atual.prox
        return None


    def busca_aluno(self, matricula):
        resultados = []
        atual_uni = self.universidades
        while atual_uni:
            atual_aluno = atual_uni.inicioAluno
            while atual_aluno:
                if atual_aluno.matricula == matricula:
                    resultados.append((atual_aluno.nome, atual_uni.nome))
                atual_aluno = atual_aluno.prox
            atual_uni = atual_uni.prox

        if resultados:
            print("Aluno encontrados com matrícula {:02d}:".format(matricula))
            for nome, nome_uni in resultados:
               
                print("Aluno {} encontra-se na universidade {}.".format(nome, nome_uni))
            
        else:
            print("Aluno não encontrado.")
        return None


    def remove_universidade(self, nome):
        universidade = self.busca_universidade(nome)
        if universidade == None:
            print("Universidade não encontrada.")
            return

        while(True):
            if universidade.inicioAluno == None:
                self.remove_aluno(universidade.inicioAluno.matricula, from_universidade=universidade)
            break
            

        if universidade.ant == None:
            self.universidades = universidade.prox
        else:
            universidade.ant.prox = universidade.prox

        if universidade.prox:
            universidade.prox.ant = universidade.ant

        print("Universidade {} removida com sucesso.".format(nome))

    def remove_aluno(self, matricula, from_universidade = None):
        if from_universidade:
            universidade = from_universidade
        else:
            universidade = self.busca_universidade_por_aluno(matricula)

    
        if universidade == None:
            print("Aluno não encontrado.")
            return
        
        alunos_encontrados = []
        atual_uni = self.universidades
        
      
        while atual_uni:
            atual_aluno = atual_uni.inicioAluno
            while atual_aluno:
                if atual_aluno.matricula == matricula:
                    alunos_encontrados.append((atual_aluno, atual_uni)) 
                atual_aluno = atual_aluno.prox
            atual_uni = atual_uni.prox

        if alunos_encontrados == None:
            print("Aluno não encontrado.")
            return

      
        if len(alunos_encontrados) > 1:
            print("Foram encontrados os seguintes alunos com a matrícula {:02d}:".format(matricula))
            for i, (aluno, nome_uni) in enumerate(alunos_encontrados):
                print(f"{i + 1}: {aluno.nome} na universidade {nome_uni.nome}")

            escolha = int(input("Digite o número do aluno que deseja remover: ")) - 1

            if escolha < 0 or escolha >= len(alunos_encontrados):
                print("Escolha inválida.")
                return
        
            aluno_selecionado, universidade = alunos_encontrados[escolha]
        else:
            aluno_selecionado, universidade = alunos_encontrados[0]
            

        atual = universidade.inicioAluno
        while atual:
            if atual.matricula == aluno_selecionado.matricula:
                if atual.ant == None:
                    universidade.inicioAluno = atual.prox
                else:
                    atual.ant.prox = atual.prox

                if atual.prox:
                    atual.prox.ant = atual.ant

                universidade.qtdAlunos -= 1
                print("\nAluno: {} \nMatrícula: {:02d} \nUniversidade: {} \nFoi removido com sucesso.".format(atual.nome, matricula, universidade.nome))
                return
            atual = atual.prox

        print("Aluno não encontrado.")

    def busca_universidade_por_aluno(self, matricula):
        atual_uni= self.universidades
        while atual_uni:
            atual_aluno = atual_uni.inicioAluno
            while atual_aluno:
                if atual_aluno.matricula == matricula:
                    return atual_uni  
                atual_aluno = atual_aluno.prox  
            atual_uni = atual_uni.prox
        return None  

   


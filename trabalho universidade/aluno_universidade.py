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
        self.qtd_alunos = 0
        self.prox = None
        self.ant = None
        self.inicio_aluno = None

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

            while(True):
                if atual == None and atual.nome < nome:
                        break
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
                while(True):
                    atual.ant = nova_uni
                    if atual == None:
                        break
                    
        nova_uni = nome
        print("Universidade {} inserida com sucesso.".format(nome))

    def insere_aluno(self, nome_uni, nome, matricula, idade, nro_disciplinas):
        universidade = self.busca_universidade(nome_uni)
        if not universidade:
            print("Universidade não encontrada.")
            opcao = input("Deseja tentar outra universidade? (1 para sim, qualquer outra tecla para não): ")
            if opcao == "1":
                nome_uni = input("Informe o nome da nova universidade: ")
                self.insere_aluno(nome_uni, nome, matricula, idade, nro_disciplinas)
            return

        novo_aluno = Aluno(nome, matricula, idade, nro_disciplinas)

        # Inserir aluno por ordem crescente de matrícula
        if universidade.inicio_aluno is None:
            universidade.inicio_aluno = novo_aluno
        else:
            atual = universidade.inicio_aluno
            anterior = None

            while atual is not None and atual.matricula < matricula:
                anterior = atual
                atual = atual.prox

            if anterior is None:
                novo_aluno.prox = universidade.inicio_aluno
                universidade.inicio_aluno.ant = novo_aluno
                universidade.inicio_aluno = novo_aluno
            else:
                anterior.prox = novo_aluno
                novo_aluno.ant = anterior
                novo_aluno.prox = atual
                if atual is not None:
                    atual.ant = novo_aluno

        universidade.qtd_alunos += 1
        print("Aluno {} inserido com sucesso na universidade {}.".format(nome, nome_uni))
       

    def busca_universidade(self, nome):
        atual = self.universidades
        while atual is not None:
            if atual.nome == nome:
                return atual
            atual = atual.prox
        return None


    def busca_aluno(self, matricula):
        atual_uni = self.universidades
        while atual_uni is not None:
            atual_aluno = atual_uni.inicio_aluno
            while atual_aluno is not None:
                if atual_aluno.matricula == matricula:
                    print(f"Aluno encontrado: {atual_aluno.nome} na universidade '{atual_uni.nome}'.")
                    return atual_aluno
                atual_aluno = atual_aluno.prox
            atual_uni = atual_uni.prox
        print("Aluno não encontrado.")
        return None


    def remove_universidade(self, nome):
        universidade = self.busca_universidade(nome)
        if not universidade:
            print("Universidade não encontrada.")
            return

        # Remover todos os alunos da universidade
        while(True):
            if universidade.inicio_aluno == None:
                self.remove_aluno(universidade.inicio_aluno.matricula, from_universidade=universidade)
            break
            
        # Ajustar a lista de universidades
        if universidade.ant == None:
            self.universidades = universidade.prox
        else:
            universidade.ant.prox = universidade.prox

        if universidade.prox is not None:
            universidade.prox.ant = universidade.ant

        print(f"Universidade '{nome}' removida com sucesso.")

    def remove_aluno(self, matricula, from_universidade=None):
        if from_universidade:
            universidade = from_universidade
        else:
            universidade = self.busca_universidade_por_aluno(matricula)

        if not universidade:
            print("Aluno não encontrado.")
            return

        atual = universidade.inicio_aluno
        while atual is not None:
            if atual.matricula == matricula:
                if atual.ant is None:
                    universidade.inicio_aluno = atual.prox
                else:
                    atual.ant.prox = atual.prox

                if atual.prox is not None:
                    atual.prox.ant = atual.ant

                universidade.qtd_alunos -= 1
                print(f"Aluno de matrícula '{matricula}' removido com sucesso.")
                return
            atual = atual.prox

        print("Aluno não encontrado.")

    def busca_universidade_por_aluno(self, matricula):
        atual = self.universidades
        while(True): 
            if atual == None:
                atual_aluno = atual.inicio_aluno
            while(True):
                if atual_aluno.matricula == matricula:
                    atual_aluno == None
                    return atual
                atual_aluno = atual_aluno.prox
                atual = atual.prox
                return None





# Aplicação da inserção
#lista = Lista()
#uni = "USP"
#lista.insere(uni)
#lista.imprime()
#uni = "UFMG"
#lista.insere(uni)
#lista.imprime()
#lista.reverso()
#lista.insere(uni)
#lista.imprime()
#lista.reverso()
#lista.insere(uni)
from aluno_universidade import Aluno
from aluno_universidade import Universidade
from aluno_universidade import Lista

#Adicionando universidades

def menu():
    print("\nSeja bem vindo(a)!")
    programa = Lista()
    while True: 
        print("\nMenu:")
        print("1) Insere Universidade")
        print("2) Insere Aluno")
        print("3) Busca Universidade")
        print("4) Busca Aluno")
        print("5) Remove Universidade")
        print("6) Remove Aluno")
        print("0) Fechar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome da universidade: ")
            programa.insere_universidade(nome)
        elif opcao == "2":
            nome_uni = input("Nome da universidade: ")
            nome = input("Nome do aluno: ")
            matricula = int(input("Matrícula do aluno: "))
            idade = int(input("Idade do aluno: "))
            nroDisciplinas = int(input("Número de disciplinas: "))
            programa.insere_aluno(nome_uni, nome, matricula, idade, nroDisciplinas)
        elif opcao == "3":
            nome = input("Nome da universidade: ")
            universidade = programa.busca_universidade(nome)
            if universidade:
                print("Universidade {} encontrada com {} alunos.".format(nome, universidade.qtdAlunos))
            else:
                print("Universidade não encontrada.")
        elif opcao == "4":
            matricula = int(input("Matrícula do aluno: "))
            programa.busca_aluno(matricula)
        elif opcao == "5":
            nome = input("Nome da universidade: ")
            programa.remove_universidade(nome)
        elif opcao == "6":
            matricula = int(input("Matrícula do aluno: "))
            programa.remove_aluno(matricula)
        elif opcao == "0":
            print("Fechando o programa...")
            break
        else:
            print("Opção inválida.")



# Aplicação da inserção
#programa = Lista()
#nome = "USP"
#programa.imprime(nome)
#programa.busca_universidade(nome)
#programa.remove_universidade(nome)
#nome = "Guilherme"
#matricula = 202401111
#sistema.insere_aluno("USP","Guilherme", 2024010605, "20anos", 10)
#sistema.busca_aluno(nome)
#sistema.remove_aluno(nome)


if __name__ == "__main__":
    menu()
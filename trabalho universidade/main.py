from aluno_universidade import Aluno
from aluno_universidade import Universidade
from aluno_universidade import Lista

#Adicionando universidades

def menu():
    sistema = Lista()
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
            sistema.insere_universidade(nome)
        elif opcao == "2":
            nome_uni = input("Nome da universidade: ")
            nome = input("Nome do aluno: ")
            matricula = int(input("Matrícula do aluno: "))
            idade = int(input("Idade do aluno: "))
            nro_disciplinas = int(input("Número de disciplinas: "))
            sistema.insere_aluno(nome_uni, nome, matricula, idade, nro_disciplinas)
        elif opcao == "3":
            nome = input("Nome da universidade: ")
            universidade = sistema.busca_universidade(nome)
            if universidade:
                print(f"Universidade '{nome}' encontrada com {universidade.qtd_Alunos} alunos.")
            else:
                print("Universidade não encontrada.")
        elif opcao == "4":
            matricula = int(input("Matrícula do aluno: "))
            sistema.busca_aluno(matricula)
        elif opcao == "5":
            nome = input("Nome da universidade: ")
            sistema.remove_universidade(nome)
        elif opcao == "6":
            matricula = int(input("Matrícula do aluno: "))
            sistema.remove_aluno(matricula)
        elif opcao == "0":
            print("Fechando o sistema...")
            break
        else:
            print("Opção inválida.")

# Aplicação da inserção
sistema = Lista()
nome = "USP"
sistema.insere_universidade(nome)
sistema.busca_universidade(nome)
#sistema.remove_universidade(nome)
nome = "Guilherme"
#matricula = 202401111
sistema.insere_aluno("USP","Guilherme", 2024010605, "20anos", 10)
#sistema.busca_aluno(nome)
#sistema.remove_aluno(nome)
#sistema.imprime()
#uni = "UFMG"
#lista.insere(uni)
#lista.imprime()
#lista.reverso()
#lista.insere(uni)
#lista.imprime()
#lista.reverso()
#lista.insere(uni)






if __name__ == "__main__":
    menu()
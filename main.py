from aluno import Aluno
from disciplina import Disciplina
from professor import Professor #type: ignore
from diretor import Diretor #type: ignore
from funcionário import Funcionario #type: ignore
from pessoa import Pessoa

disciplinas_disponiveis = []

disc = Disciplina("POO", "Alyson", 64, "LEC1")
disciplinas_disponiveis.append(disc)

disc = Disciplina("Matemática", "Carlão", 32, "I2118")
disciplinas_disponiveis.append(disc)

aluno = Aluno("12345657845", "2024123123", "Alyson", "ECA", ["POO", "Técnicas de Programação", "Matemática"], disciplinas_disponiveis)
aluno2 = Aluno("2024321321", "José", "ECA", ["POO", "Técnicas de Programação", "Eletrônica", "Matemática Computacional", "Malabarismo", "ChatGPT"], disciplinas_disponiveis)

professor = Professor("20243213210", "1234567", "Josevaldo", "ECA", ["POO"], disciplinas_disponiveis)


diretor = Diretor("56789012345", "752675621", "Robson", "ECA", ["Matematica"], disciplinas_disponiveis)

funcinário = Funcionario("89012345678", "5678901234", "Armando", "", [], disciplinas_disponiveis)

professor.define_bonus()
print(professor.salario)

print(aluno.disciplinas)

print(aluno.insere_disciplina("Ciências Humanas", disciplinas_disponiveis))

for disc in aluno.disciplinas:
    print(disc.nome)

aluno.remove_disciplina("POO")

print("\n\n")
for disc in aluno.disciplinas:
    print(disc.nome)

#print(aluno.historico.imprime_historico())
from aluno import Aluno
from disciplina import Disciplina

disciplinas_disponiveis = []

disc = Disciplina("POO", "Guilherme", 64, "LECI")
disciplinas_disponiveis.append(disc)

disc = Disciplina("Calculo Z", "Euler", 32, "I2118")
disciplinas_disponiveis.append(disc)

aluno = Aluno("2024010605", "Guilherme","ECA", ["POO", "Técnicas de Programação", "Eletronica", "Calculo Z"], disciplinas_disponiveis)

print(aluno.disciplinas)

if aluno.insere_disciplina("Calculo Z", disciplinas_disponiveis):
    print("Aluno matriculado")
else:
    print("Aluno não matriculado")


for x in range (len(aluno.disciplinas)):
    print(aluno.disciplinas(x).nome)

aluno.imprime_aluno ()

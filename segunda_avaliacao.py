class No:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.esquerda = None
        self.direita = None
        self.altura = 1  # altura inicial de cada nó é 1 (porque um nó isolado tem altura 1)

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def direita_rotação(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = max(self.altura(y.esquerda), self.altura(y.direita)) + 1
        x.altura = max(self.altura(x.esquerda), self.altura(x.direita)) + 1

        return x

    def esquerda_rotação(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        x.altura = max(self.altura(x.esquerda), self.altura(x.direita)) + 1
        y.altura = max(self.altura(y.esquerda), self.altura(y.direita)) + 1

        return y

    def insere(self, raiz, pessoa):
        if not raiz:
            return No(pessoa)

        # Inserir no lugar correto (ordem alfabética pelo nome)
        if pessoa.nome < raiz.pessoa.nome:
            raiz.esquerda = self.insere(raiz.esquerda, pessoa)
        else:
            raiz.direita = self.insere(raiz.direita, pessoa)

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        balance = self.balanceamento(raiz)

        # Caso 1: Rotação à direita
        if balance > 1 and pessoa.nome < raiz.esquerda.pessoa.nome:
            return self.direita_rotação(raiz)

        # Caso 2: Rotação à esquerda
        if balance < -1 and pessoa.nome > raiz.direita.pessoa.nome:
            return self.esquerda_rotação(raiz)

        # Caso 3: Rotação à esquerda-direita
        if balance > 1 and pessoa.nome > raiz.esquerda.pessoa.nome:
            raiz.esquerda = self.esquerda_rotação(raiz.esquerda)
            return self.direita_rotação(raiz)

        # Caso 4: Rotação à direita-esquerda
        if balance < -1 and pessoa.nome < raiz.direita.pessoa.nome:
            raiz.direita = self.direita_rotação(raiz.direita)
            return self.esquerda_rotação(raiz)

        return raiz

    def insere_pessoa(self, pessoa):
        self.raiz = self.insere(self.raiz, pessoa)

    def busca(self, raiz, cpf):
        if raiz == None or raiz.pessoa.cpf == cpf:
            return raiz

        if cpf > raiz.pessoa.cpf:
            return self.busca(raiz.esquerda, cpf)
        elif cpf < raiz.pessoa.cpf:
            return self.busca(raiz.esquerda, cpf)
        else:
            return self.busca(raiz.direita, cpf)

    def remover(self, raiz, cpf):
        if not raiz:
            return raiz

        if cpf > raiz.pessoa.cpf:
            raiz.direita = self.remover(raiz.direita, cpf)
        elif cpf < raiz.pessoa.cpf:
            raiz.esquerda = self.remover(raiz.esquerda, cpf)
        else:
            if raiz.direita == None:
                return raiz.esquerda
            elif raiz.esquerda == None:
                return raiz.direita
            

            temp = self.obter_minimo(raiz.direita)
            raiz.pessoa = temp.pessoa
            raiz.direita = self.remover(raiz.direita, temp.pessoa.cpf)
            
             

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        balance = self.balanceamento(raiz)

        if balance > 1 and self.balanceamento(raiz.esquerda) >= 0:
            return self.direita_rotação(raiz)

        if balance < -1 and self.balanceamento(raiz.direita) <= 0:
            return self.esquerda_rotação(raiz)

        if balance > 1 and self.balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.esquerda_rotação(raiz.esquerda)
            return self.direita_rotação(raiz)

        if balance < -1 and self.balanceamento(raiz.direita) > 0:
            raiz.direita = self.direita_rotação(raiz.direita)
            return self.esquerda_rotação(raiz)

        return raiz

    def obter_minimo(self, raiz):
        while raiz.esquerda:
            raiz = raiz.esquerda
        return raiz

    def arvore_hierárquica(self, no, level=0):
        if no is not None:
            self.arvore_hierárquica(no.direita, level + 1)
            print(" " * (level * 8) + str(no.pessoa.nome))
            self.arvore_hierárquica(no.esquerda, level + 1)

    def imprimir_em_ordem(self, no):
        if no:
            self.imprimir_em_ordem(no.esquerda)
            print(no.pessoa.nome)
            self.imprimir_em_ordem(no.direita)

class Pessoa:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

# Teste da árvore AVL com pessoas
avl = ArvoreAVL()

# Lista de pessoas (com CPFs repetidos)
pessoas = [
    Pessoa("Guilherme Castro", "11223344556", "Rua C, 789", "3333-3333"),
    Pessoa("Ana Silva", "12345678901", "Rua A, 123", "1111-1111"),
    Pessoa("Carlos Oliveira", "98765432100", "Rua B, 456", "2222-2222"),
    Pessoa("Maria Costa", "22334455667", "Rua D, 101", "4444-4444"),
    Pessoa("Neymar Santos", "33445566778", "Rua E, 202", "5555-5555"),
    Pessoa("Roberta Lima", "44556677889", "Rua F, 303", "6666-6666"),
    Pessoa("Vini Jr", "55667788990", "Rua G, 404", "7777-7777"),
    Pessoa("Fernanda Almeida", "66778899001", "Rua H, 505", "8888-8888"),
    Pessoa("Davi Narciso", "12309845677", "Rua I, 777", "4002-8922"),
    Pessoa("Leonardo Silva", "40028922369", "Rua J, 666", "1234-5678"),
    Pessoa("Ana Silva", "12345678901", "Rua A, 123", "1111-1111"),  # CPF repetido
    Pessoa("Carlos Oliveira", "98765432100", "Rua B, 456", "2222-2222")  # CPF repetido
]



# Inserindo pessoas na árvore (após verificar se o CPF já existe)
for pessoa in pessoas:
    if avl.busca(avl.raiz, pessoa.cpf):
        print(f"CPF {pessoa.cpf} já existe. Pessoa não inserida.")
    else:
        avl.insere_pessoa(pessoa)




# Exibindo a árvore AVL em formato hierárquico
print("\nÁrvore AVL hierárquica:")
avl.arvore_hierárquica(avl.raiz)
print("\n")

# Removendo duas pessoas
avl.raiz = avl.remover(avl.raiz, "55667788990")  # Removendo Vini Jr
avl.raiz = avl.remover(avl.raiz, "12345678901")  # Removendo Ana Silva

print("Remoção feita!")
print("\n")

# Exibindo a árvore AVL após remoções
print("Árvore AVL após remoções:")
avl.arvore_hierárquica(avl.raiz)
print("\n")

# Imprimindo os nomes em ordem alfabética (ordem de visita em uma árvore AVL)
print("\nLista de nomes em ordem alfabética:")
avl.imprimir_em_ordem(avl.raiz)


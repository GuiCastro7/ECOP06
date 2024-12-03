class No:
    def __init__(self, num):
        self.num = num
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
        x = y.esquerda      # Identifica o novo nó raiz (subárvore esquerda de y)
        T2 = x.direita      # Subárvore direita de x (que será movida)

        # Rotação
        x.direita = y       # y se torna o filho direito de x
        y.esquerda = T2     # T2 se torna o filho esquerdo de y

        # Atualiza as alturas
        y.altura = max(self.altura(y.esquerda), self.altura(y.direita)) + 1
        x.altura = max(self.altura(x.esquerda), self.altura(x.direita)) + 1

        return x

    def esquerda_rotação(self, x):
        y = x.direita       # Identifica o novo nó raiz (subárvore direita de x)
        T2 = y.esquerda     # Subárvore esquerda de y (que será movida)

        # Rotação
        y.esquerda = x      # x se torna o filho esquerdo de y
        x.direita = T2      # T2 se torna o filho direito de x

        # Atualiza as alturas
        x.altura = max(self.altura(x.esquerda), self.altura(x.direita)) + 1
        y.altura = max(self.altura(y.esquerda), self.altura(y.direita)) + 1

        return y

    def insere(self, raiz, num):
        if not raiz:
            return No(num)

        # Inserir no lugar correto
        if num < raiz.num:
            raiz.esquerda = self.insere(raiz.esquerda, num)
        else:
            raiz.direita = self.insere(raiz.direita, num)

        # Atualiza a altura do nó ancestral
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        # Verificar o fator de balanceamento para garantir que a árvore se mantenha balanceada
        balance = self.balanceamento(raiz)

        # Caso 1: Rotação à direita
        if balance > 1 and num < raiz.esquerda.num:
            return self.direita_rotação(raiz)

        # Caso 2: Rotação à esquerda
        if balance < -1 and num > raiz.direita.num:
            return self.esquerda_rotação(raiz)

        # Caso 3: Rotação à esquerda-direita
        if balance > 1 and num > raiz.esquerda.num:
            raiz.esquerda = self.esquerda_rotação(raiz.esquerda)
            return self.direita_rotação(raiz)

        # Caso 4: Rotação à direita-esquerda
        if balance < -1 and num < raiz.direita.num:
            raiz.direita = self.direita_rotação(raiz.direita)
            return self.esquerda_rotação(raiz)

        return raiz

    def insere_num(self, num):
        self.raiz = self.insere(self.raiz, num)

    # Método para exibir a árvore de maneira hierárquica (horizontal)
    def arvore_hierárquica(self, no, level=0):
        if no is not None:
            # Primeiro imprime a subárvore direita, para posicioná-la no topo visual
            self.arvore_hierárquica(no.direita, level + 1)
            # Imprime o nó atual, com indentação proporcional ao nível
            print(" " * (level * 8) + str(no.num))
            # Depois imprime a subárvore esquerda
            self.arvore_hierárquica(no.esquerda, level + 1)

    # Método para exibir a árvore em forma de pirâmide
    def arvore_em_piramide(self, no):
        if not no:
            return

        altura = self.altura(no)
        largura = 2 ** altura - 2

        fila = [(no, largura // 2)]
        espacos_entre = largura

        while fila:
            nivel_proximo = []
            linha = ""

            for no, posicao in fila:
                if no:
                    linha += " " * (posicao - len(linha)) + str(no.num)
                    nivel_proximo.append((no.esquerda, posicao - espacos_entre // 3))
                    nivel_proximo.append((no.direita, posicao + espacos_entre // 3))
                else:
                    linha += " " * (posicao - len(linha))
                    nivel_proximo.append((None, 0))

            print(linha)
            espacos_entre //= 2
            fila = [no for no in nivel_proximo if no[0]]


# Teste da árvore AVL
avl = ArvoreAVL()

# Inserindo os valores na árvore
valores = [9, 5, 1, 3, 10, 4, 6, 7]
for val in valores:
    avl.insere_num(val)

# Exibindo a árvore com a estrutura hierárquica (raízes e filhos)
print("Visualização de uma arvore AVL hierarquicamente:")
avl.arvore_hierárquica(avl.raiz)
print("\n")

# Exibindo a árvore AVL no formato em pirâmide
print("Árvore AVL em formato de pirâmide:")
avl.arvore_em_piramide(avl.raiz)
print("\n")

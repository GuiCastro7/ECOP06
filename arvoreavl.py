class No:
    def __init__(self, key):
        self.key = key
        self.esquerda = None
        self.direita = None
        self.altura = 1  # altura inicial de cada nó é 1 (porque um nó isolado tem altura 1)

class ArvoreAVL:
    def __init__(self):
        self.root = None

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def balance_factor(self, no):
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

    def insere(self, root, key):
        if not root:
            return No(key)

        # Inserir no lugar correto
        if key < root.key:
            root.esquerda = self.insere(root.esquerda, key)
        else:
            root.direita = self.insere(root.direita, key)

        # Atualiza a altura do nó ancestral
        root.altura = 1 + max(self.altura(root.esquerda), self.altura(root.direita))

        # Verificar o fator de balanceamento para garantir que a árvore se mantenha balanceada
        balance = self.balance_factor(root)

        # Caso 1: Rotação à direita
        if balance > 1 and key < root.esquerda.key:
            return self.direita_rotação(root)

        # Caso 2: Rotação à esquerda
        if balance < -1 and key > root.direita.key:
            return self.esquerda_rotação(root)

        # Caso 3: Rotação à esquerda-direita
        if balance > 1 and key > root.esquerda.key:
            root.esquerda = self.esquerda_rotação(root.esquerda)
            return self.direita_rotação(root)

        # Caso 4: Rotação à direita-esquerda
        if balance < -1 and key < root.direita.key:
            root.direita = self.direita_rotação(root.direita)
            return self.esquerda_rotação(root)

        return root

    def insere_key(self, key):
        self.root = self.insere(self.root, key)

    # Metodo de exibir em ordem a arvore AVL (linear)
    def ordem(self, root):
        if root:
            self.ordem(root.esquerda)
            print(root.key, end=" ")
            self.ordem(root.direita)

    # Método para exibir a árvore de maneira hierárquica (raízes)
    def arvore_hierárquica(self, no, level=0):
        if no is not None:
            # Primeiro imprime a subárvore direita, para posicioná-la no topo visual
            self.arvore_hierárquica(no.direita, level + 1)
            # Imprime o nó atual, com indentação proporcional ao nível
            print(" " * (level * 8) + str(no.key))
            # Depois imprime a subárvore esquerda
            self.arvore_hierárquica(no.esquerda, level + 1)

# Teste da árvore AVL
avl = ArvoreAVL()

# Inserindo os valores na árvore
valores = [15, 5, 25, 3, 10, 20, 30, 7]
for val in valores:
    avl.insere_key(val)

# Exibindo a árvore AVL em ordem
print("Árvore AVL em ordem :")
avl.ordem(avl.root)
print("\n")

# Exibindo a árvore com a estrutura hierárquica (raízes e filhos)
print("Visualização de uma arvore AVL hierarquicamente:")
avl.arvore_hierárquica(avl.root)
print("\n")

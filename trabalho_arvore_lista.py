import random

class No: # Usado para as duas classes
    def __init__(self, num):
        self.num = num
        self.prox = None  # Utilizado para o funcionamento da lista
        self.esquerda = None  # Usado na árvore
        self.direita = None   # Usado na árvore

class Lista:
    def __init__(self):
        self.ini = None
        self.qtdLista = 0
    
    def buscar(self, num):
        # Busca linear na lista
        atual = self.ini
        busca = 0
        while atual:
            busca += 1
            if atual.num == num:
                return busca  # Se encontrar o número, retorna o número de iterações 
            atual = atual.proximo
        return busca  # Se não encontrar, retorna o número de busca
    
    def insere_lista(self, num):
        novo_no = No(num)

        if self.ini == None:
            self.ini = novo_no
            return

        aux = self.ini
        while(True):
            if aux.prox == None or aux.prox.num > num:
                break
            aux = aux.prox
            self.qtdLista += 1

        if aux.prox == None and num > aux.num: #último elemento
            aux.prox = novo_no
        elif aux == self.ini: #primeiro elemento
            novo_no.prox = self.ini
            self.ini = novo_no
        else:
            novo_no.prox = aux.prox
            aux.prox = novo_no

class Arvore:
    def __init__(self):
        self.raiz = None
        self.qtdArvore = 0
    
    def buscar(self, num):
        # Busca binária na árvore
        atual = self.raiz
        busca = 0
        while atual:
            busca += 1
            if num < atual.num:
                atual = atual.esquerda
            elif num > atual.num:
                atual = atual.direita
            else:
                return busca  # Encontrou o número
        return busca  # Não encontrou o número
    
    def insere_arvore(self, num):
        self.qtdArvore += self.buscar(num)
        
        # Caso a árvore esteja vazia, insere o primeiro nó
        if self.raiz == None:
            self.raiz = No(num)
            return True

        
        atual = self.raiz
        while True:
            self.qtdArvore += 1  # Incrementa a contagem de buscas realizadas
            if num < atual.num:
                if atual.esquerda:
                    atual = atual.esquerda
                else:
                    atual.esquerda = No(num)
                    return True
            elif num > atual.num:
                if atual.direita:
                    atual = atual.direita
                else:
                    atual.direita = No(num)
                    return True
            else:
                # Se o núemro ja existir na árvore, não acontece a inserção
                return False

def geracao_numeros_unicos():
    numeros = []
    numeros_gerados = set() #Verifica a unicidade
    
    for i in range(5000):  # Gera exatamente 5000 números
        while True:
            numero = random.randint(0, 100000)
            if numero in numeros_gerados:
                break  # Sai do loop e gera outro número
            else:
                numeros_gerados.add(numero)
                numeros.append(numero)
                break #Sai do loop porque o número foi encontrado e adicionado
    
    return numeros


#Aplicação dos numeros na lista e arvore. 
lista = Lista()
arvore = Arvore()
numeros_gerados = geracao_numeros_unicos()  # Gera 5000 números únicos

for numero in numeros_gerados:
    lista.insere_lista(numero)
    arvore.insere_arvore(numero)

#Impressão sobre a quantidade de buscas feitas tanto na lista quanto no código e qual a diferença(numérica) nesse caso
print("Quantidade total de buscas obtidas na lista e na árvore foram:\nLista: {} \nÁrvore: {}".format(lista.qtdLista, arvore.qtdArvore))

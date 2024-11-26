import random

class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None  # Para lista
        self.esquerda = None  # Para árvore
        self.direita = None   # Para árvore

class Lista:
    def __init__(self):
        self.ini = None
        self.qtdLista = 0
    
    def buscar(self, valor):
        # Busca linear na lista
        atual = self.ini
        busca = 0
        while atual:
            busca += 1
            if atual.valor == valor:
                return busca  # Encontrou o valor
            atual = atual.proximo
        return busca  # Retorna o número de iterações (não encontrou)
    
    def insere_lista(self, num):
        novo_no = No(num)

        if self.ini == None:
            self.ini = novo_no
            return

        aux = self.ini
        while(True):
            if aux.prox == None or aux.prox.valor > num:
                break
            aux = aux.prox
            self.qtdLista += 1

        if aux.prox == None and num > aux.valor: #último elemento
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
    
    def buscar(self, valor, no):
        # Busca binária na árvore
        busca = 0
        while no:
            busca += 1
            if valor < no.valor:
                no = no.esquerda
            elif valor > no.valor:
                no = no.direita
            else:
                return busca  # Encontrou o valor
        return busca  # Não encontrou o valor
    
    def insere_arvore(self, valor):
        # Conta a quantidade de buscas feitas ao tentar inserir
        busca = self.buscar(valor, self.raiz)
        self.qtdArvore += busca  # Soma as buscas feitas

        if busca == 0:  # O número não está na árvore
            novo_no = No(valor)
            if not self.raiz:
                self.raiz = novo_no
            else:
                self._inserir_no(self.raiz, novo_no)
            return True
        return False
    
    def _inserir_no(self, no_atual, novo_no):
        # Método auxiliar para inserir recursivamente na árvore
        self.qtdArvore += 1
        if novo_no.valor < no_atual.valor:
            if no_atual.esquerda:
                self._inserir_no(no_atual.esquerda, novo_no)
            else:
                no_atual.esquerda = novo_no
        else:
            if no_atual.direita:
                self._inserir_no(no_atual.direita, novo_no)
            else:
                no_atual.direita = novo_no

def gerar_numeros_unicos():
    numeros = []
    numeros_gerados = set()  # Para verificar unicidade
    
    while len(numeros) < 5000:
        numero = random.randint(0, 100000)
        if numero not in numeros_gerados:
            numeros_gerados.add(numero)
            numeros.append(numero)
    
    return numeros

def main():
    lista = Lista()
    arvore = Arvore()
    numeros_gerados = gerar_numeros_unicos()  # Gera 5000 números únicos

    for numero in numeros_gerados:
        lista.insere_lista(numero)
        arvore.insere_arvore(numero)

    print(f"Quantidade total de buscas na lista: {lista.qtdLista}")
    print(f"Quantidade total de buscas na árvore: {arvore.qtdArvore}")

if __name__ == "__main__":
    main()

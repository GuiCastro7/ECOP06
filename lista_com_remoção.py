class No():
    def __init__(self, num):
        self.num = num
        self.prox = None

class Lista():
    def __init__(self):
        self.ini = None

    def insere(self, num):
        novo_no = No(num)

        if self.ini == None:
            self.ini = novo_no
            return

        aux = self.ini
        while(True):
            if aux.prox == None or aux.prox.num > num:
                break
            aux = aux.prox
        
        if aux.prox == None and num > aux.num: #último elemento
            aux.prox = novo_no
        elif aux == self.ini: #primeiro elemento
            novo_no.prox = self.ini
            self.ini = novo_no
        else:
            novo_no.prox = aux.prox
            aux.prox = novo_no

    def remove(self, num):
        if self.ini == None:  # lista vazia
            return
        
        aux = self.ini
        while (True):
            if aux == None or aux.num == num :  # chegou ao final da lista
                break
            ant = aux
            aux = aux.prox

        if aux == None:
            print("Elemento não encontrado.")
            return
        if aux == self.ini:  # encontrou o elemento
            self.ini = aux.prox  # Atualiza o ponteiro para o próximo nó
            del aux # libera a memória do nó encontrado
            return
              
        if aux.prox == None:
            ant.prox = None
            del aux  # libera a memória do primeiro nó
            return

        ant.prox = aux.prox
        del aux



    def imprime(self):
        aux = self.ini
        print("\n\n")
        while(True):
            print(aux.num)
            aux = aux.prox

            if aux == None:
                break


lista = Lista()
lista.insere(27)
lista.imprime()
lista.insere(40)
lista.imprime()
lista.insere(20)
lista.imprime()
lista.insere(74)
lista.imprime()
lista.insere(56)
lista.imprime()
lista.insere(100)
lista.imprime()
lista.insere(7)
lista.imprime()
lista.insere(1)
lista.imprime()
lista.insere(90)
lista.imprime()
lista.insere(0)
lista.imprime()
lista.insere(10)
lista.imprime()

lista.remove(27)  # Remove do início
lista.imprime()
lista.remove(56)  # Remove do meio
lista.imprime()
lista.remove(95) # Tenta remover elemento que não existe
lista.imprime()
lista.remove(10)  # Remove do fim
lista.imprime()
lista.remove(3)   # Tenta remover elemento que não existe
lista.imprime()
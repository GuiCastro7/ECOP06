class No:
    def __init__(self, num):
        self.num = num
        self.prox = None
        self.ant = None  # Ponteiro para o nó anterior

class Lista:
    def __init__(self):
        self.ini = None
        self.fim = None

    def insere(self, num):
        novo_no = No(num)

        if self.ini == None:
            self.ini = novo_no
            return

        aux = self.ini
        while (True):
            if aux.prox == None or aux.num > num:
                break
            aux = aux.prox

        if aux.prox == None and num > aux.num:  # Último elemento
            aux.prox = novo_no
            novo_no.ant = aux
        elif aux == self.ini:  # Primeiro elemento
            novo_no.prox = self.ini
            self.ini.ant = novo_no
            self.ini = novo_no
        else:
            novo_no.prox = aux
            aux.ant.prox = novo_no
            novo_no.ant = aux.ant
            aux.ant = novo_no
            


    def imprime(self):
        aux = self.ini
        print("\n")
        while(True):
            print(aux.num)
            aux = aux.prox
            if aux == None:
                break
    
    def reverso(self):
        aux = self.ini
        print("\n")
        while(True):
            if aux.prox == None: # Ir para o último nó
                break
            aux = aux.prox

        print("\nImpressão reversa:")
        while(True): 
            print(aux.num)
            aux = aux.ant
            if aux == None:
                break
            


# Aplicação da inserção
lista = Lista()
lista.insere(27)
#lista.imprime()
lista.insere(40)
#lista.imprime()
lista.reverso()
lista.insere(20)
#lista.imprime()
lista.reverso()
lista.insere(74)
#lista.imprime()
lista.reverso()
lista.insere(10)
#lista.imprime()
lista.reverso()
lista.insere(30)
#lista.imprime()
lista.reverso()
lista.insere(26)
#lista.imprime()
lista.reverso()
lista.insere(47)
#lista.imprime()
lista.reverso()
lista.insere(36)
lista.imprime()
lista.reverso()



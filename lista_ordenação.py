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

    def imprime(self):
        aux = self.ini
        print("\n")
        while(True):
            print(aux.num)
            aux = aux.prox

            if aux == None:
                break

# Aplicação da inserção

lista = Lista()
lista.insere(27)
#lista.imprime()
lista.insere(40)
#lista.imprime()
lista.insere(20)
#lista.imprime()
lista.insere(74)
lista.imprime()

       
       
       
       
       
       
       
       
       
       
       
       
       
#Parte abaixo feito com o Alysson        
        #if aux == self.ini #1 elemento
        #elif aux = None  #elemento final
        #else #elemento do meio

        
    #def imprime(self):
        #atual = self.ini
        #elementos []
        #print(self.prox)
        #print(self.meio)


#lista = Lista()
#lista.insere(4)
#lista.insere(3)
#lista.insere(6)
#lista.imprime()

#print(lista.imprime())

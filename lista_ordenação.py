class No():
    def __init__(self, num):
        self.num = num
        self.prox = None

class Lista():
    def __init__(self):
        self.ini = None
    
    def insere(self, num):
        novo_no = No(num)
      
    #Novo elemento com lista vazia   
        if  self.ini == None:
            self.ini = novo_no
            return
        
    # Caso o novo dado seja menor que o da cabeça, insere no início
        if num < self.ini.num:
            novo_no.prox = self.ini
            self.ini = novo_no
            return
        
        atual = self.ini
            
    #Parte com o allyson 
        #while(True):
            #aux = self.ini
            #if aux.num < num:  
                #aux = aux.prox

    # Percorre a lista para encontrar a posição correta
        while atual.prox and atual.prox.num < num:
            atual = atual.prox

    # Insere no fim se chegamos ao final da lista
        novo_no.prox = atual.prox
        atual.prox = novo_no

    def imprime(self):
        atual = self.ini
        elementos = []
        while atual:
            elementos.append(atual.num)
            atual = atual.prox
        return elementos



# Aplicação da inserção
if __name__ == "__main__":
    lista = Lista()
    lista.insere(10)
    lista.insere(5)
    lista.insere(7)
    lista.insere(15)
    
print(lista.imprime())  # Saída: [5, 7, 10, 15]
       
       
       
       
       
       
       
       
       
       
       
       
       
       
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
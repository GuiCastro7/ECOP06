class No:
    def __init__(self, num):
        self.num = num
        self.esquerda = None
        self.direita = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def insere(self, raiz, num):
        if raiz is None:  # Se a raiz está vazia, cria o nó e retorna
            novo_no = No(num)
            raiz = novo_no
            return raiz  

        if num < raiz.num:  
            raiz.esquerda = self.insere(raiz.esquerda, num)  #Se o num for menor que a raiz ele vai para a esquerda
        else:  
            raiz.direita = self.insere(raiz.direita, num) # Caso a raiz seja menor que o numero inserido, o numero inserido vai para a direita

        return raiz 



    def imprime(self, raiz): #Verifica se é None, se for ele cai no return e volrta pra verificação.
        if raiz == None:
                return
        
        self.imprime(raiz.esquerda) # Se não tiver nada pra esquerda ele retorna e imprime a raiz desse
        print(raiz.num)
        self.imprime(raiz.direita) # Se não tiver na direita ele retorna para a raiz e verifica o None




arvore = Arvore()
arvore.raiz = arvore.insere(arvore.raiz, 5) 
arvore.raiz = arvore.insere(arvore.raiz, 3)  
arvore.raiz = arvore.insere(arvore.raiz, 7)  
arvore.raiz = arvore.insere(arvore.raiz, 2)  
arvore.raiz = arvore.insere(arvore.raiz, 4)  
arvore.raiz = arvore.insere(arvore.raiz, 6)  
arvore.raiz = arvore.insere(arvore.raiz, 8)  


arvore.imprime(arvore.raiz)

print("Fim")

class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None  # Lista começa vazia
    
    def adicionar_no_inicio(self, dado):
        """Adiciona um novo nó no início da lista."""
        novo_no = No(dado)  # Cria um novo nó com o dado
        novo_no.prox = self.topo  # O ponteiro do novo nó aponta para o topo antigo
        self.topo = novo_no  # O topo agora é o novo nó
    
    def desempilhar(self):
        """Remove o nó no topo da pilha."""
        if not self.topo:
            print("Pilha vazia! Não há elementos para remover.")
            return
        self.topo = self.topo.prox
        

    def exibir_lista(self):
        """Exibe os elementos da lista."""
        atual = self.topo
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.prox
        print("None")  # Final da lista

lista = Pilha()



lista.adicionar_no_inicio(10)
lista.adicionar_no_inicio(40)
lista.adicionar_no_inicio(30)
lista.adicionar_no_inicio(20)
lista.adicionar_no_inicio(15)
lista.adicionar_no_inicio(50)
lista.adicionar_no_inicio(47)

print("\nLista antes da remoção:")
lista.exibir_lista()  

lista.desempilhar()
print("\nLista após a remoção:")
lista.exibir_lista() 


lista.desempilhar()  
print("\nLista após a remoção:")
lista.exibir_lista() 

lista.desempilhar() 
print("\nLista após a remoção:")
lista.exibir_lista()  


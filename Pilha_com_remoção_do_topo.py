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
        
        # O topo da pilha aponta para o próximo nó
        topo_removido = self.topo
        self.topo = self.topo.prox
        topo_removido = None  # Libera o nó removido

    def exibir_lista(self):
        """Exibe os elementos da lista."""
        atual = self.topo
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.prox
        print("None")  # Final da lista

# Criando a lista ligada
lista = Pilha()

# Adicionando elementos ao início da lista
lista.adicionar_no_inicio(10)
lista.adicionar_no_inicio(20)
lista.adicionar_no_inicio(30)

# Exibindo a lista
print("Lista antes da remoção:")
lista.exibir_lista()  # Saída: 30 -> 20 -> 10 -> None

lista.desempilhar()  # Remover o valor 30

# Exibindo a lista após a remoção
print("Lista após a remoção:")
lista.exibir_lista()  # Esperado: 20 -> 10 -> None

lista.desempilhar()  # Remover o valor 20

print("Lista após a remoção:")
lista.exibir_lista()  # Esperado: 10 -> None


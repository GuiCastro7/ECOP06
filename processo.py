import time

class Processo():

    def __init__ (self, nome, prioridade, taxaCompleto, taxaPorCiclo, tempoProcessamento):
        self.nome = nome
        self.prioridade = prioridade
        self.taxaCompleto = taxaCompleto        
        self.taxaPorCiclo = taxaPorCiclo
        self.tempoProcessamento = tempoProcessamento
        self.prox = None

class Lista():
    def __init__(self):
        self.ini = None

    def insere(self, novo_processo):

        if self.ini == None:
            self.ini = novo_processo
            novo_processo.prox = novo_processo
            return
        
        aux = self.ini

        while(True):
            if aux.prox == self.ini or aux.prox.prioridade > novo_processo.prioridade:
                novo_processo.prox = aux.prox
                aux.prox = novo_processo
                break
            aux = aux.prox
        

    def remove(self, processo):
        if self.ini == None: 
            print("Lita vazia")
            return
        

        
        if self.ini == self.ini.prox and self.ini == processo:
            self.ini = None
            return

        
        if self.ini == processo:
            aux = self.ini
            while (True):
                if aux.prox == self.ini:
                    break
                aux = aux.prox
            self.ini = self.ini.prox
            aux.prox = self.ini
            return

        
        aux = self.ini
        while (True): 
            if aux.prox == self.ini:
                break
            
            if aux.prox == processo:
                aux.prox = aux.prox.prox
                return
            aux = aux.prox
            




    def processar(self):
        if self.ini == None:
            return

        aux = self.ini
        print("\n\n")
        while True:
            if aux.taxaCompleto >= 100:
                self.remove(aux)
                print("{} foi finalizado".format(aux.nome))
                if self.ini == None:
                    break
                aux = self.ini
            else:
                print("{} entrou no processador".format(aux.nome))
                time.sleep(aux.tempoProcessamento)
                aux.taxaCompleto += aux.taxaPorCiclo
                if aux.taxaCompleto > 100:
                    aux.taxaCompleto = 100
                print("{} saiu do processador com taxa de {}%".format(aux.nome, aux.taxaCompleto))
                if aux.taxaCompleto < 100:
                    print("{} atualizado para {}%".format(aux.nome, aux.taxaCompleto))
                if aux.prox == self.ini:
                    break
                aux = aux.prox

        


# Criando os processos iniciais 
p1 = Processo("Processo 1", 1, 0, 20, 1)
p2 = Processo("Processo 2", 2, 0, 40, 2)
p3 = Processo("Processo 3", 2, 0, 25, 3)


lista = Lista()
lista.insere(p1)
lista.insere(p2)
lista.insere(p3)


lista.processar()

# Inserindo novos processos
p4 = Processo("Processo 4", 2, 0, 35, 4)
p5 = Processo("Processo 5", 1, 0, 50, 5)
lista.insere(p4)
lista.insere(p5)

lista.processar()
lista.processar()

# Remoção de um processo
lista.remove(p5)
print("{} foi removido com sucesso.".format(p5.nome))

lista.processar()
lista.processar()
lista.processar()
lista.processar()
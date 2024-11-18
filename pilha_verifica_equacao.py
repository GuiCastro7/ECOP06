class No():
    def __init__(self, char):
        self.num = char
        self.prox = None

class Pilha():
    def __init__(self):
        self.topo = None

    def verificaEquacao(self, eq):
        for c in eq:
            if c == "(":
                self.push("(")
            elif c == ")":
                if self.pop() == False:
                    print("Equação errada")
                    return
                
        if self.topo == None:
            print("Equação correta")
        else:
            print("Equação errada")

    def push(self, char):
        novo_no = No(char)

        if self.topo != None:
            novo_no.prox = self.topo
        
        self.topo = novo_no
        print(novo_no.prox)

    def pop(self):
        if self.topo == None:
            return False

        aux = self.topo
        self.topo = self.topo.prox

        return aux


eq = input("Insira a equação: ")
pilha = Pilha()
pilha.verificaEquacao(eq)

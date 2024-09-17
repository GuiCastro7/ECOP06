class ArCondicionado():
    def __init__(self, id, qtdResf):
        self.id = id
        self.on = False
        self.qtdResf = qtdResf


    def ativado(self):
        self.on = True

    def desativado(self):
        self.on = False

    def esta_ativado(self):
        return self.on
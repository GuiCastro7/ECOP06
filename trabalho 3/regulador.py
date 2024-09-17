class Regulador():
    def __init__(self, id, qtdPress):
        self.id = id
        self.on = False
        self.qtdResf = qtdPress


    def ativado(self):
        self.on = True

    def desativado(self):
        self.on = False

    def esta_ativado(self):
        return self.on
from funcionário import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, login, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self.login = login
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

gerente = Gerente("Carlos", "12345678900", "15000", "login", "senha", 10)
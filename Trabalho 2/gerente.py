from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, num_matricula, funcionarios=None):
        super().__init__(nome, cpf, num_matricula)
        self.funcionarios = funcionarios if funcionarios is not None else []

    def cria_pessoa(self):
        return f"Gerente: {self.nome}, CPF: {self.cpf}, Matrícula: {self.num_matricula}"

    def adicionar_funcionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.funcionarios.append(funcionario)
            return f"Funcionário {funcionario.nome} adicionado à lista de funcionários."
        else:
            return "O objeto fornecido não é uma instância de Funcionario."

    def listar_funcionarios(self):
        if not self.funcionarios:
            return "Nenhum funcionário sob responsabilidade do gerente."
        lista = "Funcionários sob responsabilidade do gerente: {}\n".format(self.nome)
        for func in self.funcionarios:
            lista += f"- {func.nome}, Matrícula: {func.num_matricula}\n"
        return lista


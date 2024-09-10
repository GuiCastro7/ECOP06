from cliente import Cliente
from funcionario import Funcionario 
from gerente import Gerente 
from conta_poupanca import Conta_Poupanca
from conta_corrente import Conta_Corrente




# Criando clientes
cliente1 = Cliente("Guilherme Castro", "123.456.789-00", "C001")
# Criando funcionários
funcionario1 = Funcionario("Guilherme Silva", "111.222.333-44", "F001")
funcionario2 = Funcionario("Guilherme Narciso", "109.283.475.66", "F002")
# Criando gerente com uma lista de funcionários
gerente = Gerente("Roberto Costa", "999.888.777-66", "G001")

 # Adicionar funcionários ao gerente
print("\n")
print(gerente.adicionar_funcionario(funcionario1))
print(gerente.adicionar_funcionario(funcionario2))

 # Listar funcionários
print(gerente.listar_funcionarios())

# Criando contas
conta_corrente_cliente1 = Conta_Corrente(1001, "001", cliente1)
conta_poupanca_cliente1 = Conta_Poupanca(1002, "001", cliente1, 10)

# Exibindo informações dos clientes e funcionários
print(f"Conta criada! Seja bem vindo(a).")
print(cliente1.cria_pessoa())
print(gerente.cria_pessoa())

# Operações com contas
conta_corrente_cliente1.deposito(500.00)
conta_corrente_cliente1.saque(200.00)
print(conta_corrente_cliente1.extrato())

conta_poupanca_cliente1.deposito(300.00)
conta_poupanca_cliente1.saque(130.00)
print(conta_poupanca_cliente1.extrato())





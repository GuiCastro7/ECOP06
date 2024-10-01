from datetime import datetime
from hotel import ControleReserva, Funcionario, ExcecaoReserva




if __name__ == "__main__":
    controle_reserva = ControleReserva()
    
    while True:
        nome = input("Nome do hóspede: ")
        cpf = input("CPF do hóspede: ")
        cod = int(input("Código da Reserva: "))
        numero_quarto = int(input("Número do quarto: "))
        data = datetime.strptime(input("Data da Reserva (dd/mm/aa): "), "%d/%m/%y")
        funcionario_nome = input("Funcionário: ")
        funcionario = Funcionario(funcionario_nome, "123.456.789.00", 2500)  # Exemplo fixo, pode ser adaptado
        

        #controle_reserva = ControleReserva("Guilherme Castro", "123.456.789-00", "123", "07", "11/10/24", "Castro")
        try:
            controle_reserva.cria_reservas(nome, cpf, cod, numero_quarto, data, funcionario)
            print("Reserva concluída!")
        except ExcecaoReserva as e:
            print("Não é possível fazer a reserva, o quarto já está reservado.")
            
        op = input("Deseja realizar nova reserva (sim ou não)? ")
        if op.lower() != "sim":
            break
        
    controle_reserva.imprime_reservas()       

    #Lista de quartos disponíveis:
    #Quarto 1 = Simples, Valor: 50))
    #Quarto 2 = Simples, Valor: 50))
    #Quarto 3 = Simples, Valor: 50))
    #Quarto 4 = Duplo, Valor: 100))
    #Quarto 5 = Duplo, Valor: 100))
    #Quarto 6 = Luxo, Valor: 200))

    
            
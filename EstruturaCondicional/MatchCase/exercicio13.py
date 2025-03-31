





salarioatual = float(input("Digite o salário anual atual do funcionário: R$ "))

cargoatual = str(input("Digite o cargo atual do funcionário: "))

tempo = int(input("Digite o tempo de serviço do funcionário em anos: "))

if cargoatual == "Gerente":
    match tempo:
        case tempo if tempo > 0 and tempo < 3:
            print(f"Aumento do salário anual de 8%. Novo salário anual: R$ {salarioatual*1.08:.2f}")

        case tempo if tempo >= 3 and tempo < 5:
            print(f"Aumento do salário anual de 9%. Novo salário anual: R$ {salarioatual*1.09:.2f}")

        case tempo if tempo >= 5:
            print(f"Aumento do salário anual de 10%. Novo salário anual: R$ {salarioatual*1.10:.2f}")
            
        case _:
            print('Tempo inválido')
            

if cargoatual == "Engenheiro":
    match tempo:
        case tempo if tempo > 0 and tempo < 3:
            print(f"Aumento do salário anual de 9%. Novo salário anual: R$ {salarioatual*1.09:.2f}")

        case tempo if tempo >= 3 and tempo < 5:
            print(f"Aumento do salário anual de 10%. Novo salário anual: R$ {salarioatual*1.10:.2f}")

        case tempo if tempo >= 5:
            print(f"Aumento do salário anual de 11%. Novo salário anual: R$ {salarioatual*1.11:.2f}")
            
        case _:
            print('Tempo inválido')
            
            
if cargoatual == "Técnico":
    match tempo:
        case tempo if tempo > 0 and tempo < 3:
            print(f"Aumento do salário anual de 10%. Novo salário anual: R$ {salarioatual*1.10:.2f}")

        case tempo if tempo >= 3 and tempo < 5:
            print(f"Aumento do salário anual de 11%. Novo salário anual: R$ {salarioatual*1.11:.2f}")

        case tempo if tempo >= 5:
            print(f"Aumento do salário anual de 12%. Novo salário anual: R$ {salarioatual*1.12:.2f}")
            
        case _:
            print('Tempo inválido')


tempogasto = float(input("Digite o tempo gasto da viagem em horas: "))
velocidademedia = float(input("Digite a velocidade média durante a viagem em km/h (quilômetros por hora): "))

litrosgasto = float(tempogasto*velocidademedia/10.5)

print(f"A quantidade de litros gastos na viagem é: {litrosgasto:.4f}")
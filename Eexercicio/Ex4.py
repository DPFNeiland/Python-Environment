

QtdDeAndaimesDpsPLoc = int(input("Digite a quantidade de andaimes disponíveis para locação: "))

ValDiarioAluguelCadaAndaime = float(input("Digite o valor diário do aluguel de cada andaime (em reais R$): "))

print(f"Faturamento anual com aluguéis> R$ {QtdDeAndaimesDpsPLoc*0.4*30*12*ValDiarioAluguelCadaAndaime:.2f}")

print(f"Ganho mensal com multas R$ {QtdDeAndaimesDpsPLoc*0.4*0.08*ValDiarioAluguelCadaAndaime*0.15*12:.2f}")

print(f"Quantidade de andaimes ao final do ano: {QtdDeAndaimesDpsPLoc*1.15:.0f}")
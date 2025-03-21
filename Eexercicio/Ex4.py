

QtdDeAndaimesDpsPLoc = int(input("Digite a quantidade de andaimes disponíveis para locação (maior que 0): "))

if (QtdDeAndaimesDpsPLoc <= 0):
    print('Digite um valor válido para a quantidade de andaimes disponíveis para locação.')
    
else:
    ValDiarioAluguelCadaAndaime = float(input("Digite o valor diário do aluguel de cada andaime em reais R$ (maior que 0): "))

    if (ValDiarioAluguelCadaAndaime <=0):
        print('Digite um valor válido para o valor diário do aluguel por andaime.')
        
    else:
        
        print(f"Faturamento anual com aluguéis: R$ {QtdDeAndaimesDpsPLoc*0.4*30*12*ValDiarioAluguelCadaAndaime:.2f}")

        print(f"Ganho mensal com multas: R$ {QtdDeAndaimesDpsPLoc*0.4*0.08*ValDiarioAluguelCadaAndaime*0.15*12:.2f}")

        print(f"Quantidade de andaimes ao final do ano: {QtdDeAndaimesDpsPLoc*1.15:.0f}")
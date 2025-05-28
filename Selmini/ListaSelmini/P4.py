


sM = float(input("Digite o valor do salário mínimo em R$: "))

n = int(input("Digite o número de contribuintes: "))

lS = []
lD = []

for i in range(0, n):
    
    lS.append(float(input(f"Digite o salário do {i+1}º contribuinte: ")))
    lD.append(int(input(f"Digite o número de dependentes do {i+1}º contribuinte: ")))
    
    lS[i] = lS[i]*(1 - lD[i]*0.05)
    
    if lS[i] < 0:
        lS[i] = 0
    
    if lS[i] < 2*sM:
        print("Esse contribuinte é isento do importo de renda")
    
    elif lS[i] >= 2*sM and  lS[i] < 3*sM:
        print(f"O valor do I.R desse contribuinte é: R$ {lS[i]*0.05:.2f}")
    
    elif lS[i] >= 3*sM and  lS[i] < 5*sM:
        print(f"O valor do I.R desse contribuinte é: R$ {lS[i]*0.1:.2f}")
        
    elif lS[i] >= 5*sM and  lS[i] < 7*sM:
        print(f"O valor do I.R desse contribuinte é: R$ {lS[i]*0.15:.2f}")
        
    elif lS[i] >= 7*sM:
        print(f"O valor do I.R desse contribuinte é: R$ {lS[i]*0.20:.2f}")
    
    else:
        print("O salário mínimo é inválido.")
        
    
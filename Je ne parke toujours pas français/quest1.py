



inicio = int(input("Digite o início, pae: "))
# 20

fim = int(input("Digita o fim: "))
# 10

if inicio > fim:
    inicio, fim = fim, inicio
    
for i in range(inicio, fim+1):
    
    divisoresLimites = int(i/2) + 1
        
    soma = 0
    
    for j in range(1, divisoresLimites):
        
        if i % j == 0:
            soma += j

    if soma == i:
        print(f'{i} é perfeito (ingual eu)')
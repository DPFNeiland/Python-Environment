
inicio, fim = -1, -1

while inicio < 1 or fim < 1:
    inicio = int(input('Informe o início do intervalo (>= 1): '))
    fim = int(input('Informe o fim desse intervalo (>= 1): '))


if inicio > fim:
    inicio, fim = fim, inicio

qtd_pft = 0

for i in range(inicio, fim + 1):
    
    soma = 0
    
    for divisao in range(1, i // 2 + 1):
        
        if i % divisao == 0:
            soma += divisao
            
    if soma == i:
        qtd_pft += 1        
print(f'Quantidade de números perfeitos no intervalo de {inicio} a {fim}: {qtd_pft}')
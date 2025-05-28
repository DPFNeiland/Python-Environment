from math import sqrt

numero = int(input("Digite um número: "))
maior = -1

for h in range(2, numero): 
    if numero % h == 0:  
        ehprimo = True
        
        for i in range(2, int(sqrt(h)) + 1):
            if h % i == 0:
                ehprimo = False
                break
        if ehprimo:
            maior = h

print(f'Maior fator primo de {numero} é {maior}')


from random import randint
from math import inf

def calcular_soma(i):
    
    soma = 0
    for j in range(n):
        soma += v[i + j]
        
    return soma
        
v = [randint(0, 10) for i in range(10)]

n = randint(1, len(v) - 1)

maximo = -inf
minimo = inf

print(v)
print(n)

for i in range(len(v)-n + 1):
    soma = calcular_soma(i)
    
    maximo = max(maximo, soma)    
    minimo = min(minimo, soma)
    
print(f"{minimo} {maximo}")

from random import randint

def contar(grade):
    n = len(grade)
    total = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            cont = bin(grade[i] & grade[j]).count("1")
                
            total += (cont*(cont-1)) // 2
            
    return total

def Imprimir_grade(grade):
    for i in range(M):
        for j in range(M): 
            print(grade[i][j], end="\t")
        print()

M = 333

imagem = [[(randint(0,1)) for _ in range(M)] for _ in range(M)]
numeros = []

for i in range(M):
    numero = 0
    for j in range(M):
        numero |= (imagem[i][M-j-1]) << j
    
    numeros.append(numero)

total = contar(numeros)

print(f"total de subgrades = {total}")

from random import randint

ORDEM = 3

lista = [[randint(0, ORDEM**2) for _ in range(ORDEM)] for _ in range(ORDEM)] 

print(lista)

diagonalP = 0
diagonalS = 0
for i in range(0,ORDEM):
    diagonalP += lista[i][i]
    diagonalS += lista[i][ORDEM-1-i]
    
print(diagonalP)
print(diagonalS)

    
    


cont = 0
from math import log2

for n in range(2, 77):
    for i in range(n):
        for j in range(i, n):
            cont += 1
    
    print(f"{n} -> {cont} | {n*log2(n)} | {n*n}")
    cont = 0
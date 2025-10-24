from random import randint

def contar(grade):
    n = len(grade)
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            cont = 0
            for k in range(n):
                if grade[i][k] == 1 and grade[j][k]:
                    cont +=1
            total += (cont*(cont-1)) // 2
            
    return total

M = 300

imagem = [[(randint(0,1)) for _ in range(M)] for _ in range(M)]

print(imagem)

for i in range(M):
    for j in range(M):
        print(imagem[i][j], end="\t")
    print()
    
total = contar(imagem)

print(f"total de subfgrades = {total}")
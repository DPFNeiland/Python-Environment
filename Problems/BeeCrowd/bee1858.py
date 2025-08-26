


N = int(input())

numeros = list(map(int, input().split()))

iMax = -1
numMin = 999

for i in range (0, len(numeros)):
    if numMin > numeros[i]:
        numMin = numeros[i]
        iMax = i + 1
        
print(iMax)
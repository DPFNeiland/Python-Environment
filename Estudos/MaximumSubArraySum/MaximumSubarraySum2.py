
lista = [312, 517, 7, -322, -153, 1302]


# lista = list(map(int,input().split()))

N = len(lista)

best = 0

for i in range(0,N):
    sum = int(0)
    
    for j in range(i,N):
        sum += lista[j]
        best = max(best,sum)
        
print(best)
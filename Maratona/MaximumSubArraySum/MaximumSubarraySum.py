

lista = [312, 517, 7, -322, -153, 1302]

# lista = list(map(int,input().split()))

N = len(lista)

best = int(0)

for i in range (0,N):
    for j in range (i,N):
        sum = int(0)
        
        for k in range (i,j):
            sum += lista[k]
        
        best = max(best,sum)
        
print(best)
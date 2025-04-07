


lista = list(map(int,input().split()))

N = len(lista)

best = int(0)

sum = int(0)

for i in range(0,N):
    sum = max(lista[i], sum+lista[i])
    best = max(best,sum)
    
print(best)
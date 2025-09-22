from math import inf


N = int(input())

dismax = -inf
raio =  inf

x = []
y = []

for i in range(N):
    auxX, auxY = input().split()
    
    x.append(int(auxX))
    y.append(int(auxY))
    
    if i != 0:
        if x[i] == x[i-1]:
            dis = abs(y[i] - y[i-1])

        if y[i] == y[i-1]:
            dis = abs(x[i] - x[i-1])
            
        dismax = max(dis, dismax)
        raio = min(raio, dis - 1)
            

if dismax > 2*raio:
    raio = -1
    
print(raio)
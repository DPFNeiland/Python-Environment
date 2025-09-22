from math import inf

N, K = input().split()

N = int(N)
K = int(K)
k = K

x = (list(map(int, input().split())))

resp = 0
for i in range(N):
    minimo = inf
    k = K                           
    xCopia = x.copy()
    
    for j in range(i, max(-1, i-K), -1):
        xCopia[j] += k
        k -= 1


    for j in range(N):
        minimo = min(minimo, xCopia[j])
    
    resp = max(minimo, resp)
    
print(resp)
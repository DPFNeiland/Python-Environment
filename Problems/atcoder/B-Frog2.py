
from math import inf

def custo(i):
    
    if i == 0:
        return 0
    
    if values[i] != -1:
        return values[i]
    
    ret = inf
    for j in range(max(0,i - K),i):
        ret = min(ret, custo(j) + abs(h[i] - h[j])) 

    values[i] = ret
    return values[i]



N, K = list(map(int,input().split()))
h = list(map(int, input().split()))

values = [-1] * (N)


print(custo(N-1))

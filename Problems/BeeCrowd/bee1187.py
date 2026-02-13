
M = 12
soma = 0
q = [[0 for _ in range(M)] for _  in range(M)]

n = M - 1
o = 1

S = input()

for i in range(M):
    for j in range(M):
        aux = float(input())
        
        q[i][j] = aux


for i in range(5):
    for j in range(o, n, 1):
        soma += q[i][j]
        
    n -= 1
    o += 1
    
    
if S == 'S':
    print(f"{soma:.1f}")

elif S == 'M':
    print(f"{soma/30.0:.1f}")
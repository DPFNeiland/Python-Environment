
M = 12
soma = 0
n = [[0 for _ in range(M)] for _  in range(M)]

K = int(input())
S = input()

for i in range(M):
    for j in range(M):
        aux = float(input())
        
        n[i][j] = aux

for i in range(M):
    soma += n[K][i]
    
if S == 'S':
    print(f"{soma:.1f}")

elif S == 'M':
    print(f"{soma/12.0:.1f}")
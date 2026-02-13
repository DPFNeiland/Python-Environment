


N, M = input().split()
N = int(N)
M = int(M)

G = [list(map(int, input().split())) for _ in range(N)]



resp = 0
for i in range(M):
    maximo = 0
    for j in range(N):
        maximo = max(maximo,G[j][i])
    resp += maximo
    
print(resp)
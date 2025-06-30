

M, N = input().split()

M = int(M)
N = int(N)

estoque = [[0 for _ in range(N)] for _ in range(M)]

for i in range(M):
    estoque[i] = list(map(int, input().split()))
        
P = int(input())

total = 0

for i in range(P):
    i, j = input().split()
    i = int(i) - 1
    j = int(j) - 1

    if(estoque[i][j] - 1 < 0 ):
        pass
    else:
        estoque[i][j] -= 1
        total += 1 

print(total)
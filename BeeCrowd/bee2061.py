


N, M = [int(x) for x in input().split()]

for i in range(0,M):
    acao = str(input())
    
    if(acao == "fechou"):
        N+=1
    else:
        N-=1

print(N)
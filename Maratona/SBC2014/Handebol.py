



N, M = [int(i) for i in input().split()]

resp = 0

for i in range(0,N):
    A = list(map(int, input().split()))
    
    aux = True
    for i in A:
        if(i == 0):
            aux = False

    if aux:
        resp+=1

print(resp)
        
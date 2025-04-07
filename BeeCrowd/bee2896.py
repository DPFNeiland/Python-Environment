


t = int(input())

for i in range(0,t):
    N, K = input().split()
    
    N = int(N)
    K = int(K)
    
    resp = 0
    while N >= K:
        N -= K
        resp += 1
    
    resp += N
    
    print(resp)
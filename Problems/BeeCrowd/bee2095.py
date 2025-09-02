


S = int(input())


Q = list(map(int, input().split()))
Q.sort(reverse=False)

N = list(map(int, input().split()))
N.sort(reverse=False)

resp = 0
u = 0

for i in range(S):   
    
    if N[i] < Q[u]:
        break
    
    if N[i] > Q[u]:
        resp += 1
        u += 1
        

    
print(resp)
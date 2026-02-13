

N = int(input())

resp = 0

for i in range(0,N):
    T, V = [int(i) for i in input().split()]
    resp += T*V
print(resp)    

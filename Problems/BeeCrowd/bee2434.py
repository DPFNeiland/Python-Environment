


N, S = (int(i) for i in input().split())

min = 1001

for i in range(0,N):
    aux = int(input())
    S += aux
    
    if(min>S):
        min = S
    
print(min)
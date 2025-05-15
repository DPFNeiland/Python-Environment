

N = int(input())
total = 0

for i in range (0,N):
    L, C = input().split()
    
    L = int(L)
    C = int(C)
    
    if L > C:
        total += C
        
        
print(total)
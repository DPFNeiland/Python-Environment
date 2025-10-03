
A = [1, 0, 0, 0, 0, 0, 0, 0]
B = [1, 0, 0, 0, 0, 0, 0, 0]
c = []

aux = 0
for i in range(len(A)-1, -1, -1):
    a = A[i]
    b = B[i]
    
    if aux == 0:
        if a != b :
            c.append(1)
        
        elif a == 0:
            c.append(0)
    
        else:
            c.append(0)
            aux = 1

    else: 
        if a != b:
            c.append(0)  
    
        elif a == 0:
            c.append(1)     
            aux = 0
    
        else :
            c.append(1)      

if aux == 1:
    c.append(1)

c.reverse()  
print(c)

# list(map, int(input().split()))
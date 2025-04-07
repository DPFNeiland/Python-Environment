


Num = int(input())

resp = 1

for i in range(2, Num+1 ):
    
    print(resp)
    
    
    if i%2 == 0:
        resp -= 1/i
        
    else:
        resp += 1/i
        
print(resp)
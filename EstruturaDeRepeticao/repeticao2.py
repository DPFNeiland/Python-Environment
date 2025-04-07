

maior = -1

# maior = float('-inf') 

for i in range (0,15):
    
    aux = int(input())
    
    if(i == 0):
        maior = aux
    
    
    if(maior < aux):
        maior = aux
        
        
print(maior) 
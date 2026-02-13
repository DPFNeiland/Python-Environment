
def misterio(valor):
    if valor <= 1:
        return False
    
    for i in range(2, valor):
        if valor % i == 0:
            return False
        
    return True

for i in range(99):
    print(f"{i} é primo? {misterio(i)}")
    
    
    
    
    

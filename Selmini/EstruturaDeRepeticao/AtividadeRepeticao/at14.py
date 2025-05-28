
def fatorial(x):
    total = 1
    for i in range(1,x+1):
        total *= i
        
    return total


N = float(input("Calculando a proximação de X graus: "))

resp = 0


for i in range(0,15):
    if(i%2 == 0):
        resp += (N ** (i*2))/fatorial(i*2)
    
    else:
        resp -= (N ** (i*2))/fatorial(i*2)
        
        
print(f'{resp}')
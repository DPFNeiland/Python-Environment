
def Fib(n: int):    
        
    if n == 1:
        return values[1]
    
    if n == 2:
        return values[2]
    
    if values[n] != 0:
        return values[n]
    
    values[n] = Fib(n - 1) + Fib(n - 2)
    
    return values[n]



values = [0] * 40
values[1] = 1
values[2] = 2

resp = 0

t = int(input())

for j in range(t):
    
    resp = 0
    x = int(input())
    aux = 1
    
    while x >= Fib(aux):
        aux += 1
    aux -= 1

    
    resp += Fib(aux - 1)
    x -= Fib(aux)
    
    while x != 0:
        
        if aux - 1 == 0:
            break
        
        if x >= Fib(aux):
            resp += Fib(aux - 1)
            x -= Fib(aux)
            
        aux -= 1
        
    print(resp)
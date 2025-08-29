
def calls(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    
    if readyC[n]:
        return chamadas[n]
    
    readyC[n] = True
    chamadas[n] = calls(n-1) + calls(n-2) + 2
    
    return chamadas[n] 
    
        
    
def fib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    if ready[n]:
        return values[n]

    values[n] = fib(n-1) + fib(n-2)
    ready[n] = True
    return values[n]

values = [-1] * 40
ready = [False] * 40
values[0], values[1] = 0, 1
chamadas = [-1] * 40
readyC = [False] * 40

N = int(input())

for _ in range(N):
    x = int(input())
    
    fib(x)
    calls(x)
    
    print(f"fib({x}) = {chamadas[x]} calls = {values[x]}")
    
    
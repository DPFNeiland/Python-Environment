

def fib(n: int):
    global calls


    if n == 0:
        return 0
    elif n == 1:
        return 1 
    
    values[n] = fib(n-1) + fib(n-2)
    ready[n] = True
    
    return values[n]

values = [-1] * 40
calls = [-1] * 40
ready = [False] * 40

N = int(input())


for i in range(N):
    
    x = int(input())
    
    resp = fib(x)
    
    print(f"fib({x}) = {calls[x]} calls = {resp}")
    
    
# 0 1  2   3   4   5   6  7    8 9 10
# 0 0  2   4   8   14  24 40                chamadas
# +0 +2  +2 +4  +6  +10 +16
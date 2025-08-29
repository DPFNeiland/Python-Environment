from math import pow

def TransformarCharParaInt(c: str):
    return ord(c) - ord('0')

def CalcularResto(s: str, d: int) -> int:
    base = 1%d
    res = 0
    for i in range(len(s)-1,-1,-1):
        num = TransformarCharParaInt(s[i])   
        res = (res + (num*base)%d)%d
        base = (base*10) % d
    return res

def fib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    if values[n] != -1:
        return values[n]

    values[n] = fib(n-1) + fib(n-2)
    return values[n]

values = [-1] * (10**9 + 1)
values[0], values[1] = 0, 1

while True:
    try:
        n, m = list(map(int, input().split()))

        print(f"{(fib(fib(n)))%m:.0f}")
        
    except EOFError:
        break
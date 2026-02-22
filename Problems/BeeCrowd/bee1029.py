
def fib(N: int) -> int:
    global calls
    calls +=1 

    if N == 0:
        return 0
    elif N == 1:
        return 1

    return fib(N-1) + fib(N-2)
    
N = int(input())

for i in range(N):
    x = int(input())
    
    calls = -1
    result = fib(x)
    print(f"fib({x}) = {calls} calls = {result}")

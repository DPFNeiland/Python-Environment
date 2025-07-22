
max = 1001
memo = [-1 for _ in range(max)]
memo[0], memo[1] = 1, 1

def fib(n: int):
    if memo[n] == -1:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

    

print(fib(max - 1))
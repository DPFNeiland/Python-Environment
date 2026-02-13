
max = 999
value = [-1] * max
ready = [False] * max 


def fib(n: int) -> int:
    if ready[n]: return value[n]
    
    if n <= 1:
        return 1
    
    value[n] =  fib(n-1) + fib(n-2)
    ready[n] = True
    
    return value[n]
    

# 1 1 2 3 5 8 13

def main():
    n = int(input())
    
    print(f"{n}° termo de fib é {fib(n -1 )}")
    
    
if __name__ == "__main__":
    main() 
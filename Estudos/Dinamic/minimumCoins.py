
from math import inf

max = 999 
coins = [1, 3, 4]
ready = [False]*max
value = [inf]*max

def solve(n: int) -> int:
    if n == 0:  
        return 0
    
    if ready[n]:
        return value[n]
    
    
    for c in coins:
        if n - c >= 0:
            value[n] = min(value[n], solve(n-c)+ 1) 
    ready[n] = True
    
    return value[n]        
    
    


def main():

    for x in range(max-1):
        print(f"x = {x}: {solve(x)}")

if __name__ == "__main__":
    main()
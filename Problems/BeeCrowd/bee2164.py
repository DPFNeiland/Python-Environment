from math import pow

def fib(n: float):
    
    x1 = (1+pow(5,(1/2)))/2
    x2 = (1-pow(5,(1/2)))/2
    
    resp = (pow(x1,n) - pow(x2,n)) / pow(5,1/2)
    
    return resp 

n = float(input())

print(f"{fib(n):.1f}")

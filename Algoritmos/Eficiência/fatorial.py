def fatorial(x):
    total = 1
    for i in range(1,x+1):
        total *= i
        
    return total

goal = 12*31*24*60*60*10**8
n = 1
while fatorial(n) <= goal:
    n += 1
    
print(n-1)
print(fatorial(n))
 
print(fatorial(n-1))
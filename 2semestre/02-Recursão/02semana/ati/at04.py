
def mult(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    
    elif m < 0 and n < 0:
        return mult(-m,-n)
    
    elif m < 0 and n > 0:
        return -mult(-m,n)
    
    elif m > 0 and n < 0:
        return -mult(m,-n)
        
    elif m < n:
        return mult(n,m)
    
    elif n == 1:
        return m
    
    return m + mult(m,n-1)

def main():
    m = int(input())
    n = int(input())
    
        
    print(mult(m,n)) 
    
if __name__ == "__main__":
    main()
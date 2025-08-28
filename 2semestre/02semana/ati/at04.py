
def mult(m: int, n: int):
    if m < n:
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
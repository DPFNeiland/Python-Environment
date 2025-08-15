
def mult(m: int, n: int):
    if n == 1:
        return m
    return m + mult(m,n-1)

def main():
    m = int(input())
    n = int(input())
    
    if n > m:
        m, n = n, m
        
    print(mult(m,n)) 
    
if __name__ == "__main__":
    main()
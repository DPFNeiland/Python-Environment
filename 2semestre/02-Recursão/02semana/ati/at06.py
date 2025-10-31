

def prod(m: int, n: int):
    if m == n:
        return m
    
    return m*prod(m-1,n)

def main():
    m = int(input())
    n = int(input())
    
    if n > m:
        m, n = n, m
        
    print(prod(m,n))


if __name__ == "__main__":
    main()
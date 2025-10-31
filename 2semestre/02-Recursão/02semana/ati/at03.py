

def mdc(m: int, n: int):
    if n == 0:
        return m
    
    if n > m:
        return mdc(n,m)

    return mdc(n,m%n)

def main():
    m = int(input("m: "))
    n = int(input("n: "))
    
    print(f"{mdc(m,n)}")
    
if __name__ == "__main__":
    main()
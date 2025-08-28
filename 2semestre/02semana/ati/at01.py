


def exp(x: int, n: int):
    if n == 0:
        return 1
    
    return x*exp(x,n-1)


def main():
    x = int(input("x: "))
    n = int(input("n: "))
    print(exp(x,n))
    
if __name__ == "__main__":
    main()
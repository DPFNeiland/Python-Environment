


def FactDouble(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return n*FactDouble(n-2)

def main():
    n = int(input())
    print(FactDouble(n))
    
    
if __name__ == "__main__":
    main()
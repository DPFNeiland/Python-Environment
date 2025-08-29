





def calcPell(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif ready[n]:
        return values[n]
    
    values[n] = 2*calcPell(n-1) + calcPell(n-2)
    ready[n] = True
    
    return values[n]



def main():
    global ready, values
    n = int(input("n >= 0: "))

    ready = [False] * (n + 1)
    values = [-1] * (n + 1)
    
    print(calcPell(n))
    
if __name__ == "__main__":
    main()
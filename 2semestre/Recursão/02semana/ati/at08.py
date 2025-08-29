



def calcFunc(n: int) -> int:    
    if n == 1:
        return pow(6,1/2)
    elif ready[n]:
        return value[n]
    
    value[n] = pow(6 + calcFunc(n-1),1/2) 
    ready[n] = True
    
    return value[n] 


def main():
    a = int(input("A >= 1:"))
    
    
    global ready, value 
    ready = [False] * (a + 1) 
    value = [-1] * (a + 1)
        
    print(calcFunc(a))


if __name__ == "__main__":
    main()
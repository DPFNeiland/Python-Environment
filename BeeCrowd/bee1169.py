

def graos(g):
    if g == 0:
        return 1
    
    return 2**(g) + graos(g-1)

N = int(input())



for i in range(0,N):
    X = int(input())
    X = X-1
    Y = graos(X)/12000.0
    print(f"{int(Y)} kg")
    
    # 
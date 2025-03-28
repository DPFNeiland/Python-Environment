


def recursaoSinistra (x):
    if(x == 0):
        return 0
    
    if(x == 1):
        return 0.5
    
    return 1/(2 + recursaoSinistra(x-1))

N = int(input())
    
    
print(f'{1+recursaoSinistra(N):.10f}')


def contar(m, n):
    i = 10
    res = 2
    k = 0.0
    
    while (k <= m):
        k = k + n *2 
        i = i / res
        res += 1
        
    return res

print(contar(16.5,2.1))
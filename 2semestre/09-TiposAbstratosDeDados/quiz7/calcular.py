
def calcular(a, b):
    aux = 0
    for i in range(len(a[b])):
        if(a[b][i] > aux):
            aux = a[b][i] 
    
    return aux

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(calcular(x, 1))
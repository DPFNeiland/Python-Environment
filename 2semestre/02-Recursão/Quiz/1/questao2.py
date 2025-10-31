
def minhaFuncao(x):
    aux = x[0]
    
    for i in range(len(x)):
        if x[i] > aux:
            aux = x[i]
            
    return aux
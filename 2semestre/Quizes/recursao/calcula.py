

def calcula(matriz):
    valor = 0
    indices = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
    
    for i in range(len(matriz)):
        pd = 1
        pad = 1
        for j in range(len(matriz)):
            pd *= matriz[j][indices[i][j]]
            pad *= matriz[j][indices[2 - i][j]]
        valor += pd
        valor -= pad
        
    return valor

matriz = [[2, 3, 1], [4, 5, 6], [7, 8, 9]]
resultado = calcula(matriz)

print(resultado)
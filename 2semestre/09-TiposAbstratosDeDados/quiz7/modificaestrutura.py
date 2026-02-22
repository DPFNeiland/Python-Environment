
vetor = [1, 2, 3]
matriz = [
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

def modifica_estrutura(estrutura, modificador):
    if len(modificador) == len(estrutura[0]):
        estrutura[0] = modificador[:]
    return estrutura

print(modifica_estrutura(matriz, vetor))
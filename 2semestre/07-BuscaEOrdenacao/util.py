from typing import List

# Função para realizar a busca linear em uma lista numérica. A função
# deve receber como parâmetro a lista 

def BuscaLinear(lista: List[int], valorBuscado: int) -> int:
    i = 0
    tamanho = len(lista)
    
    while i < tamanho and lista[i] != valorBuscado:    
        i += 1
        
    return -1 if tamanho == i else i

# função para ordenar uma lista
def BubbleSort(lista: List[int]) -> List:
    n = len(lista)
    
    for i in range(n):
        for j in range(i,n):
            if lista[j] < lista[i]:
                lista[j], lista[i] = lista[i], lista[j]
            
    return lista

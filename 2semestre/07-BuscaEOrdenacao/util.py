from typing import List
from random import randint

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

def SelectionSort(lista: List[int]) -> List :
    n = len(lista)
    
    for i in range(n):
        ind = i
        for j in range(i + 1, n):
            if lista[ind] > lista[j]:
                ind = j
        
        lista[i], lista[ind] = lista[ind], lista[i]
    
    return lista


def InsertionSort(lista: List[int]) -> List:
    n = len(lista)

    for i in range(1, n):
        valor = lista[i]
        j = i - 1
        while j >= 0 and valor < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1 
        lista[j + 1] = valor
        
    return lista

def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
        
    if inicio < fim:
        pivo = particionar(lista, inicio, fim)
        quicksort(lista, inicio, pivo - 1)
        quicksort(lista, pivo + 1, fim)

def particionar(lista, inicio, fim) -> int:  # retorna o índice do pivô
    
    # Primeiro elemento como pivô
    # lista[fim], lista[inicio] = lista[inicio], lista[fim]

    # último elemento como pivô
    # pivo = lista[fim]

    # # Elemento do meio como pivô
    # lista[fim], lista[fim//2 + 1] = lista[fim//2 + 1], lista[fim]

    # Randomicamente
    k = randint(inicio, fim)
    lista[k], lista[fim] = lista[fim], lista[k]
    
    
    
    pivo = lista[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j] > pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    # coloca o pivô no local correto
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1
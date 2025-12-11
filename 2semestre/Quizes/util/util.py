
from random import randint

# função para realizar a busca linear (sequencial) em uma lista numérica. A função
# deve receber como parâmetro a lista e o valor a ser localizado. A função retorna o índice
# do elemento encontrado ou, caso contrário, retorna -1
def busca_sequencial(lista: list[int], valor: int) -> int:
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  
    return -1  

#---------------------------------------------------------------------------------------------------
# função que realiza a busca binária em uma lista ordenada (a lista tem que estar ordenada)
# a função recebe como parâmetro a lista e também o valor a ser pesquisado. Se o valor for
# encontrado, a função retorna o índice. Se não for encontrado retorna -1.
def busca_binaria(lista: list[int], valor):
    ini, fim = 0, len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1

#------------------------------------------------------------------------------------------------
# função para ordenar uma lista de números inteiros em ordem crescente usando o método
# bolha (bubblesort)
def bolha(lista: list[int]) -> list[int]:
    for j in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

#-----------------------------------------------------------------------------------------------
# função para ordenar uma lista pelo método da seleção
def selecao(x):
    n = len(x)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if x[j] < x[menor]:
                menor = j

        # Troca os elementos (essa linha precisa estar dentro do laço externo)
        x[i], x[menor] = x[menor], x[i]

#---------------------------------------------------------------------------------------------
# função para ordenar uma lista pelo método de inserção
def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
        x[i + 1] = valor


#--------------------------------------------------------------------------------------
# função para ordenar uma lista pelo método quicksort (pivô como último elemento)
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
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    # coloca o pivô no local correto
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

#--------------------------------------------------------------------
# algoritmo de ordenação mergesort

def mergesort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    esquerda_ordenada = mergesort(esquerda)
    direita_ordenada = mergesort(direita)
    
    return juntar_listas(esquerda_ordenada, direita_ordenada)


def juntar_listas(esq, dir):
    i = 0  # índice da lista da esquerda (para ninguém fazer confusão entre os índices)
    j = 0  # índice da lista da direita
    resultado = []
    
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    # cuidado: é importante verificar se sobre algum elemento na 
    # lista da esquerda ou na da direita. Se sobrar algum elemento,
    # acrescenta no final da lista
    while i < len(esq):
        resultado.append(esq[i])
        i += 1

    while j < len(dir):
        resultado.append(dir[j])
        j += 1

    return resultado
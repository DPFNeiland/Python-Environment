

# Parte 1

lista = [12, -321, 412, 0, 3123, 13213, 567, -1233, 98, 10]
num = 13

def calcular_maior(lista: list):
    maior = lista[0]
    
    for i in range(len(lista)):
        if maior < lista[i]:
            maior = lista[i]
    
    return maior

def calcular_menor(lista: list):
    menor = lista[0]
    
    for i in range(len(lista)):
        if menor > lista[i]:
            menor = lista[i]
    
    return menor

def calcular_media(lista: list):
    soma = 0 
    for i in range(len(lista)):
        soma += lista[i]
    
    return soma/len(lista)

def binario(numero: int):
    
    if numero == 0:
        return 0

    lista = []
    numEmBinario = ""
    
    while numero != 1:
        lista.append(numero % 2)
        numero = numero // 2
        
    lista.append(numero%2)    
    for i in range(len(lista) - 1, -1, -1):
        numEmBinario += str(lista[i])
    
    return numEmBinario


def ordenarBubble(lista:list, forma: int):
    # forma = 0 -> crescente V forma = 1 = descrescente

    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    if forma == 0:
        return lista
    elif forma == 1:
        lista.reverse()
        return lista

def ordenarInsertion(lista:list, forma: int):
    # forma = 0 -> crescente V forma = 1 = descrescente

    for i in range(len(lista)):
        
        for j in range(i, 0, -1):
            if lista[j - 1] > lista[j]:
                lista[j], lista[j - 1] = lista[j - 1], lista[j]


    if forma == 0:
        return lista
    elif forma == 1:
        lista.reverse()
        return lista

def ordenarSelection(lista:list, forma: int):
    # forma = 0 -> crescente V forma = 1 = descrescente

    
    tamanho = len(lista)
    
    for i in range(tamanho):
        min = lista[0]
        indice = -1
        
        for j in range(i, tamanho):
            if min > lista[j]:
                min = lista[j]
                indice = j
                
        lista[i], lista[indice] = lista[indice], list[i]


    if forma == 0:
        return lista
    elif forma == 1:
        lista.reverse()
        return lista
    
def hexa(numero: int):
    
    if numero == 0:
        return 0

    lista = []
    numEmHexa = ""
    
    while numero != 1 or numero !=0:
        if numero % 16 == 10:
            lista.append('A')
        elif numero % 16 == 11:
            lista.append('B')
        elif numero % 16 == 12:
            lista.append('C')
        elif numero % 16 == 13:
            lista.append('D')
        elif numero % 16 == 14:
            lista.append('E')
        elif numero % 16 == 15:
            lista.append('F')
        elif numero <= 9:
            break
        else:
            lista.append(numero % 16)
        numero = numero // 16
    
    
    if numero % 16 == 10:
        lista.append('A')
    elif numero % 16 == 11:
        lista.append('B')
    elif numero % 16 == 12:
        lista.append('C')
    elif numero % 16 == 13:
        lista.append('D')
    elif numero % 16 == 14:
        lista.append('E')
    elif numero % 16 == 15:
        lista.append('F')
    elif numero != 0:
        lista.append(numero % 16) 
            
    
    for i in range(len(lista) - 1, -1, -1):
        numEmHexa += str(lista[i])
    
    return numEmHexa
    

# Parte 2

N = int(input("Digite a quantidade de valores a serem armazenados na lista: "))
lista = []

for i in range(N):
    lista.append(int(input()))

print(f'A diferença entre o maior valor e o menor é {calcular_maior(lista) - calcular_menor(lista)}')

# Parte 3


N = int(input("Digite a quantidade de valores a serem armazenados na lista: "))
lista = []

for i in range(N):
    lista.append(int(input()))
    
lista = ordenarBubble(lista, 0)

tamanho = len(lista)

print(f'Os três maiores valores da lista é: {lista[tamanho -1]}, {lista[tamanho - 2]}, {lista[tamanho - 3]}')


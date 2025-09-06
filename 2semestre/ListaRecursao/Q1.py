# Escreva um programa em python contendo uma função recursiva que receba como 
# parâmetro uma lista contendo números inteiros e seu tamanho. A função recursiva deverá 
# retornar o maior valor armazenado na lista.

from math import inf

def maior(l: list) -> int:
    resp = -inf
    
    for i in range(len(l)):
        if l[i] > resp:
            resp = l[i]

    return resp

def main ():
    lista = [-1, -2, -3, 1204]
    
    print(maior(lista))

if __name__ == '__main__':
    main()
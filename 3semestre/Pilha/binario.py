from collections import deque

def converter(valor: int):
    pilha = deque()
    while valor > 0:
        pilha.append(valor % 2)
        valor = valor // 2
    
    while pilha:
        print(pilha.pop(), end="")

# programa principal
valor = int(input("Informe valor inteiro e positivo: "))
binario = converter(valor)
binario
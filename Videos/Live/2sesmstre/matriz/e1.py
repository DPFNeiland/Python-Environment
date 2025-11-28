
from typing import List

def LeituraDaLista(n: int) -> List:
    lista = []

    for _ in range(n):
        aux = int(input())
        lista.append(aux)


    return lista

def RemovedorDeRepitido(lista: List) -> List:
    listaNova = []
    n = len(lista)

    for i in range(n):
        if not lista[i] in listaNova:
            listaNova.append(lista[i])

    return listaNova

# Entrada -> [2,3,2,2,2,2,4]
# Saída   -> [2,3,4]
def main():
    aux = 0
    listaResp = []
    n = int(input("Digite o número de elementos dam minha lista: "))
    lista = LeituraDaLista(n)

    print(RemovedorDeRepitido(lista))

    
if __name__ == "__main__":
    main()
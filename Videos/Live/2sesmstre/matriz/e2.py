from typing import List
from random import randint

matriz = List[List[int]]

def construir_matriz(ordem: int) -> List:
    mat = [[randint(-(ordem**2), (ordem**2)-1) for _ in range(ordem)] for _ in range(ordem)]

    return mat

def SomarValoresDiaPrincipal(mat: matriz) -> int:
    n = len(mat)
    soma = 0
    for i in range(n):
        soma += mat[i][i]

    return soma

def SomarValoresDiaSecundaria(mat: matriz) -> int:
    n = len(mat)
    soma = 0
    for i in range(n):
        soma += mat[i][n-i-1]

    return soma

def ImprimirMatriz(mat: matriz) -> None:
    n = len(mat)

    alinhamento = len(str(-n**2))

    for i in range(n):
        for j in range(n):
            print(f'{mat[i][j]:>{alinhamento}}', end=" ")
        print() 

def main():
    n = int(input("Digite a ORDEM DA MATRIZ: "))

    mat = construir_matriz(n)
    ImprimirMatriz(mat)

    print(f"A soma da diagonal principal é {SomarValoresDiaPrincipal(mat)}")
    print(f"A soma da diagonal secundária é {SomarValoresDiaSecundaria(mat)}")

if __name__ == "__main__":
    main()
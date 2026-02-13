from typing import List
from random import randint

matriz = List[List[int]]
ANOS = 10
MESES = 12
ALINHAMENTO = 8

def GerarTemperatura() -> float:
    temperatura = round(randint(-1,4)*10 + randint(0,9) + randint(0,9)/10 + randint(0,9)/100, 2)

    return temperatura

def ImprimirMatriz(mat: matriz) -> None:

    for i in range(ANOS):
        for j in range(MESES):
            print(f"{mat[i][j]:>{ALINHAMENTO}}", end=" ")
        print( )

def ImprimirLista(lis: List) -> None:

    for i in range(ANOS):
        print(f'{lis[i]:>{ALINHAMENTO}.2f}', end=" ")
    print()

# Funcionalidade A
def CriarMatriz() -> matriz:
    temperaturas = [[GerarTemperatura() for _ in range(MESES)] for _ in range(ANOS)]
    
    return temperaturas

# Funcionalidade B
def CalcularMediasCadaAno(mat: matriz) -> List:
    mediasCadaAno = []
    soma = 0

    for i in range(ANOS):
        soma = 0
        for j in range(MESES):
            soma += mat[i][j]
        mediasCadaAno.append(soma/12)

    return mediasCadaAno

# Funcionalidade C
def MaiorEMenorTemperaturaDosAnos(lis: List) -> List:
    maiorTemperatura = -20
    menorTemperatura = 50
    indices = [-1, -1]
    n = len(lis)

    for i in range(n):
        if lis[i] > maiorTemperatura:
            indices[1] = i + 1
            maiorTemperatura = lis[i]
        if lis[i] < menorTemperatura:
            indices[0] = i + 1
            menorTemperatura = lis[i]
    
    return indices

# Funcionalidade D

def ProcessarEImprimirResultados() -> None:
    mat = CriarMatriz()
    ImprimirMatriz(mat)

    print(f"Médias dos últimos {ANOS} anos: ")
    mediasTemperatura = CalcularMediasCadaAno(mat)
    ImprimirLista(mediasTemperatura)

    indices = MaiorEMenorTemperaturaDosAnos(mediasTemperatura)

    print(f"Ano com maior temperatura: {indices[1]}")
    print(f"Ano com menor temperatura: {indices[0]}")

def main():
    ProcessarEImprimirResultados()
    
if __name__ == "__main__":
    main()
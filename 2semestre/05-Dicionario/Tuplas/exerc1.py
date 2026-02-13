from random import randint
from math import inf

def Gerar_Pontos(n: int) -> list:
    
    lista = list()
    
    for _ in range(n):
        lista.append((randint(-n,n), randint(-n, n)))

    return lista


def Calcular_Distancia(x: int, y: int) -> float:
    
    return pow(x**2 + y**2,1/2)


def Calcular_Maior_Distancia(pontos: list) -> list:
    
    maior = -1
    pontosMaisDistantes = []
    
    for ponto in pontos:
        dist =  Calcular_Distancia(*ponto)
        if maior < dist:
            maior = dist
            pontosMaisDistantes = []
            pontosMaisDistantes.append(ponto)
    
        elif maior == dist:
            pontosMaisDistantes.append(ponto)

    return pontosMaisDistantes


def Calcular_Menor_Distancia(pontos: list) -> list:
    
    menor = inf
    pontosMenosDistantes = []
    
    for ponto in pontos:
        dist =  Calcular_Distancia(*ponto)
        if menor > dist:
            menor = dist
            pontosMenosDistantes = []
            pontosMenosDistantes.append(ponto)
    
        elif menor == dist:
            pontosMenosDistantes.append(ponto)

    return pontosMenosDistantes

def Calcular_Media_Pontos(pontos: list) -> list:
         
    soma = 0
    cont = 0
    
    for ponto in pontos:
        soma += Calcular_Distancia(*ponto)
        cont +=1
        
    return soma / cont


def main():
    pontos = Gerar_Pontos(n = 4)

    print(pontos)

    print(f"Pontos mais distantes da origem: {Calcular_Maior_Distancia(pontos)}")
    
    print(f"Pontos menos distantes da origem:{Calcular_Menor_Distancia(pontos)}")
    
    print(f"Distância média: {Calcular_Media_Pontos(pontos)}")
if __name__ == "__main__":
    main()
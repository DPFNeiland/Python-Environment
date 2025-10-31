from random import randint
from math import inf

def Criar_Temperaturas_Por_Ano() -> list:
    ANO = 10
    MES = 12
    
    ano_mes = [[randint(-8, 45) for _ in range(MES)] for _ in range(ANO)]
    
    return ano_mes

def Calcular_Medias_Por_Ano(ano_mes) -> list:
    ano = len(ano_mes)
    mes = len(ano_mes[0])
    medias = []
    
    for i in range(ano):
        
        mediaanual = 0
        for j in range(mes):
            mediaanual += ano_mes[i][j]
            
        medias.append(mediaanual/12) 
    
    return medias

def Imprimir_Medias_Por_Ano(medias) -> None:
    for i in range(len(medias)):
        print(f"Media ano {i+1}: {medias[i]:.2f}°")
    
def Calcular_Minima_E_Maxima_Historica(medias):
    maximo = -inf
    minimo = inf
    historico = []
    
    for media in medias:
        if media > maximo:
            maximo = media
        
        if media < minimo:
            minimo = media
    historico.append(maximo)
    historico.append(minimo)
    
    return historico
        
def main():
    matriz = Criar_Temperaturas_Por_Ano()
    
    lista = Calcular_Medias_Por_Ano(matriz)
    
    Imprimir_Medias_Por_Ano(lista)
    
    historico = Calcular_Minima_E_Maxima_Historica(lista)
    
    print(f"Máxima histórica: {historico[0]:.2f} °")
    print(f"Mínima histórica: {historico[1]:.2f} °")
    
if __name__ == "__main__":
    main()
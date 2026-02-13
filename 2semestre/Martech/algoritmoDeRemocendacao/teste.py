from typing import List, Tuple

dados = [
    ("Priyanka", 3, 4, 4, 1, 4),
    ("Justin"  , 4, 3, 5, 1, 5),
    ("Morpheus", 2, 5, 1, 3, 1)
]

genero = ["comedia", "acao", "drama", "terror", "romance"]

################################################################


# função para calcular a distância entre dois usuários
def calcular_distancia(usuario: tuple, novo: tuple) -> float:
    soma = 0
    for i in range(1, len(usuario)):
        n1 = usuario[i]
        n2 = novo[i]
        if n1 is not None and n2 is not None:
            soma += (n1-n2)**2 
    
    return soma**(1/2)

# função para encontrar o vizinho mais próximo
def mais_proximo(dados: List[Tuple], novo: Tuple) -> Tuple:

    melhor_vizi = None
    melhor_distancia = None

    for i in dados:
        d = calcular_distancia(i, novo)
        
        if (melhor_distancia is None) or (d < melhor_distancia):
            melhor_distancia = d
            melhor_vizi = i

    
    return melhor_vizi, melhor_distancia       
            
    
# função para fazer a recomendação
def recomendar(dados: List[Tuple], novo: Tuple) -> Tuple:
    vizinho, d = mais_proximo(dados, novo)

    if vizinho[0] is None or d == float("inf"):
        return novo, d

    indicacao = [None] * len(novo)
    for i in range(len(novo)):
        if novo[i] is not None:
            indicacao[i] = novo[i]
        else:
            indicacao[i] = vizinho[i]

    return vizinho, d, tuple(indicacao)

# Função principal
def main():
    # novo = ('Selmini', 1, 3, 3, 4, 3)
    novo = ('Selmini', 3, 4, 4, 1, 4)
    
    vizinho, d, ajuste = recomendar(dados, novo)
    
    print(f"{vizinho} & {d:.2f} & {ajuste}")
    
if __name__ == "__main__":
    main()    
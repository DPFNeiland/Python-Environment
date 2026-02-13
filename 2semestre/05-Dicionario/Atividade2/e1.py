
from random import randint

# a) Ler a ordem da matriz a partir do terminal. 
def Ler_Ordem_Matriz() -> tuple[int, int]:
    M = int(input("Digite a ordem M da matriz: "))
    N = int(input("Digite a ordem N da matriz: "))

    return (M, N)

# b) Preencher a matriz com valores inteiros aleatórios (utilizar o módulo random). O 
# preenchimento da matriz deverá ocorrer em uma função.  
def Criacao_e_Preencher_Matriz(m: int, n: int) -> list[list[int]]:  
    mapa = [[randint(1, 9) for _ in range(n)] for _ in range(m)]
    return mapa

# c) Imprimir a matriz em formato tabular (a impressão deverá ser ocorrer em uma função, 
# diferente da função que fez o preenchimento). 
def Imprimir_mapa(mapa: list[list]):
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            print(mapa[i][j], end=" ")
        print()



# d) Criar uma nova matriz do mesmo tamanho onde 'P' representa pico, 'V' representa vale e 'N' 
# representa ponto neutro. A geração da matriz deverá ocorrer em uma função.
def Calcular_Vale_Pico(mapa: list[list[int]]) -> list[list[str]]:
    M, N = len(mapa), len(mapa[0])
    resultado = [['N' for _ in range(N)] for _ in range(M)]

    for i in range(M):
        for j in range(N):
            viz = Calcular_Vizinhos(mapa, i, j)
            valor = mapa[i][j]
            if all(valor > v for v in viz):
                resultado[i][j] = 'P'
            elif all(valor < v for v in viz):
                resultado[i][j] = 'V'
            else:
                resultado[i][j] = 'N'
    return resultado

def Calcular_Vizinhos(matriz: list[list[int]], i: int, j: int) -> list[int]:
    M, N = len(matriz), len(matriz[0])
    viz = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (0 <= x < M) and (0 <= y < N) and not (x == i and y == j):
                viz.append(matriz[x][y])
    return viz


# e) Imprima no terminal a nova matriz em formato tabular (a impressão deve ocorrer em uma 
# função). Veja um exemplo a seguir. 
def Imprimir_resultado(mapa: list[list[str]]):    
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            print(mapa[i][j], end=" ")
        print() 
    
    

def main():
    origem = Ler_Ordem_Matriz()
    # 
    mapa = Criacao_e_Preencher_Matriz(*origem)
    
    Imprimir_mapa(mapa)
    
    Imprimir_resultado(Calcular_Vale_Pico(mapa))

if __name__ == "__main__":
    main()
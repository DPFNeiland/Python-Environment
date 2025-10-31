
from random import choice, randint

# Gerar um labirinto de caracteres. A ordem da matriz que representará o labirinto deverá ser 
# informada pelo terminal. A geração do labirinto deverá ser realizada em uma função. Veja a 
# seguir um exemplo de labirinto (a entrada e saída não precisam estar necessariamente nas 
# bordas da matriz). Veja a seguir um exemplo de labirinto.
def Gerar_Labirinto() -> list[list[str]]:
    x = [".", "#"]
    jatirado = []
    xS, yS, xE, yE = 0, 0, 0, 0
    
    n = int(input("Digite a comprimento do labirinto: "))
    m = int(input("Digite o largura do labirinto: "))

    labirinto = [[0 for _ in range(n)] for _ in range (m)]
    
    # Preencher a borda com as paredes:
    labirinto[0] = ["#"] * n
    labirinto[m - 1] = ["#"] * n
    
    for i in range(m):
        labirinto[i][0] = "#"
    for i in range(m):
        labirinto[i][n - 1] = "#"
    
    
    while (xS == xE) and (yS == yE):
        xS = randint(0, m - 1)
        yS = randint(0, n - 1)
        
        xE = randint(0, m - 1)
        yE = randint(0, n - 1)

    labirinto[xS][yS] = "S"
    labirinto[xE][yE] = "E"
        
    
    for i in range(1, m-1):
        for j in range(1, n-1):
            aux = choice(x)
            
            if not (((i == xE) and (j == yE)) or ((i == xS) and (j == yS))) :
                labirinto[i][j] = aux

                
    
    return labirinto

def imprimir_labirinto(labirinto: list[list[str]]):
    
    for linha in labirinto:
        for valor in linha:
            print(f"{valor}", end=" ")
        print()

def encontrar_coordenadas_entrada(labirinto: list[list[str]]):
        
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == "E":
                return (i, j)


# b) Uma função deverá verificar se existe ou não um caminho de 'E' até 'S'. A função deverá 
# retornar um valor booleano. No caso do labirinto mostrado no exemplo acima não há um 
# caminho entre 'E' e 'S'.
def Verificar_labirinto(labirinto, x: int, y: int):
    japassei = [[False for _ in range(len(labirinto[0]))] for _ in range (len(labirinto))]
    
    return Testar_Caminho(labirinto, japassei, x, y)
 
def Testar_Caminho(mapa: list[list[str]], japassei: list[list[bool]], x: int, y: int) -> bool:
    aux = False
    linha = len(mapa) - 1
    col = len(mapa[0]) - 1
    japassei[x][y] = True
    
    if mapa[max(x - 1, 0)][y] == "S" or mapa[min(x + 1, linha)][y] == "S" or mapa[x][min(y + 1, col)] == "S" or  mapa[x][max(y - 1, 0)] == "S":
        return True
    
    if mapa[max(x - 1, 0)][y] == "." and not japassei[max(x - 1, 0)][y]:
        aux = Testar_Caminho(mapa, japassei, max(x - 1, 0), y)
    
    if mapa[x][min(y + 1, col)] == "." and not japassei[x][min(y + 1, col)] and aux == False:
        aux = Testar_Caminho(mapa, japassei, x, min(y + 1, col))
            
    if mapa[min(x + 1, linha)][y] == "." and not japassei[min(x + 1, linha)][y] and aux == False:
        aux = Testar_Caminho(mapa, japassei, min(x + 1, linha), y)
    
    if mapa[x][max(y - 1, 0)] == "." and not japassei[x][max(y - 1, 0)] and aux == False:
        aux = Testar_Caminho(mapa, japassei, x, max(y - 1, 0))
    
    return aux


def main():

    
    labirinto = Gerar_Labirinto()

    imprimir_labirinto(labirinto)

    coordenadasEntrada = encontrar_coordenadas_entrada(labirinto)

    print(Verificar_labirinto(labirinto, *coordenadasEntrada))

if __name__ == "__main__":
    main()
from random import randint
from datetime import datetime

def gerar_Matriz() -> list:
    ORDEM = randint(2, 9)
    
    mat = [[randint(0,ORDEM**2 - 1) for _ in range(ORDEM)] for _ in range(ORDEM)]

    return mat

def print_Matriz(mat: list) -> None:
    ordem = len(mat)
    
    valor_max = (ordem**2 - 1)
    largura = len(str(valor_max))
    
    for i in range(ordem):
        for j in range(ordem):
            print(f"{mat[i][j]:>{largura}}", end=" ")
        print()
    print()
    
def Transportar_Matriz(mat: list) -> list:
    j = len(mat) - 1
    
    for i in range(len(mat)):
        mat[i][i], mat[i][j] = mat[i][j], mat[i][i]
        j -= 1  

    return mat


def main():
    global inicio
    matriz = gerar_Matriz()

    print_Matriz(matriz)
    
    matriz = Transportar_Matriz(matriz)
    
    print_Matriz(matriz)

    fim = datetime.now()
    
    print((fim-inicio).total_seconds())
    
if __name__ == "__main__":
    global inicio 
    inicio = datetime.now()
    
    
    main()
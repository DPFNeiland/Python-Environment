
from typing import List, Dict

def mochila(itens: List[Dict], capacidade: int) -> int:

    n = len(itens)
    matriz = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    
    for i in range(1, n+1):
        peso = itens[i-1].get("peso")
        valor = itens[i-1].get("valor")
        
        for j in range(1, capacidade + 1):
            valor_atual = -1
            item_anterior = matriz[i-1][j]
            
            if peso <= j:
                valor_atual = valor + matriz[i-1][j-peso]
            
            matriz[i][j] = max(item_anterior, valor_atual)

    return matriz[n][capacidade]


def main():
    itens = [
        {"valor": 500, "peso": 4},
        {"valor": 400, "peso": 2},
        {"valor": 300, "peso": 1},
        {"valor": 450, "peso": 3}
    ]
    capacidade = 5
    
    maximo = mochila(itens, capacidade)
    
    print(maximo)
    
    # print(escolhidos)

# programa principal
if __name__ == "__main__":
    main()
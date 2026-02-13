from typing import List, Dict, Tuple


# função de programação dinâmica para o problema da mochila
def mochila(itens: List[Dict], capacidade: int) -> Tuple[int, List]:
    n = len(itens)
    tabela = [[0] * (capacidade + 1) for _ in range(n +  1)]
    
    for i in range(1, n + 1):
        peso = itens[i - 1].get("peso")
        valor = itens[i - 1].get("valor")
        
        for j in range(1, capacidade + 1):
            anterior = tabela[i - 1][j]
            item_com_valor = -1
            
            if peso <= j:
                item_com_valor = valor + tabela[i - 1][j - peso]
    
            tabela[i][j] = max(anterior, item_com_valor)
    
    valor_maximo = tabela[n][capacidade]
    
    escolhidos = []
    
    for i in range(n, 0, -1):
        if tabela[i][capacidade]  != tabela[i-1][capacidade]:
            escolhidos.append(itens[i-1].get("nome"))
            capacidade -= itens[i-1].get("peso")
    
    return (valor_maximo, escolhidos)
       
# função principal
def main():
    itens = [
        {"nome": "rádio", "valor": 3000, "peso": 4},
        {"nome": "notebook", "valor": 2000, "peso": 3},
        {"nome": "violão", "valor": 1500, "peso": 1}
    ]
        
    capacidade = 5
    
    maximo, escolhidos = mochila(itens, capacidade)
    
    print(maximo)
    
    print(escolhidos)

# programa principal
if __name__ == "__main__":
    main()
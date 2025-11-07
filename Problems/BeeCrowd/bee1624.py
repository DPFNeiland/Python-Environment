
def mochila(lista: list[dict], capacidade: int) -> int:

    n = len(lista)
    matriz = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        valor = lista[i - 1].get("valor")
        peso = lista[i - 1].get("peso")
        
        for j in range(1, capacidade + 1):
            item_anterior = matriz[i-1][j]
            valor_atual = -1
            
            if peso <= j:
                valor_atual = valor + matriz[i-1][j-peso]
                
            matriz[i][j] = max(item_anterior, valor_atual)
            
            

    return matriz[n][capacidade]


n = int(input())
while n != 0:
    lista = []
    
    for i in range(n):
        valor, peso = input().split()
        item = {"valor": int(valor), "peso": int(peso)}
        
        lista.append(item)
    
    capacidade = int(input())
        
    print(mochila(lista, capacidade))    
    
    n = int(input())
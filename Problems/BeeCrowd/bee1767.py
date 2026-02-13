

def mochila(lista: list[dict], capacidade: int, qtdItens: int) -> None:

    n = len(lista)
    pesofinal = 0
    pacotesRestantes = 0
    
    matriz = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1) ]


    for i in range(1, n+1):
        qtd = lista[i-1].get("qt")
        peso = lista[i-1].get("peso")
        
        for j in range(1, capacidade + 1):
            item_anterior = matriz[i-1][j]
            qtd_atual = -1
            
            if peso <= j:
                qtd_atual = qtd + matriz[i-1][j-peso] 
                
            matriz[i][j] = max(item_anterior, qtd_atual)
    
    print(f"{matriz[n][capacidade]} brinquedos")
    for i in range(n, 0, -1):
        if matriz[i][capacidade] != matriz[i-1][capacidade]:
            peso = lista[i-1].get("peso")
            pesofinal += peso
            capacidade -= peso
            
            pacotesRestantes += 1
            
    pacotesRestantes = qtdItens - pacotesRestantes  
    
    print(f"Peso: {pesofinal} kg") 
    print(f"sobra(m) {pacotesRestantes} pacote(s)")
    print()





n = int(input())

for _ in range(n):
    qtdItens = int(input())
    lista = []
    
    for _ in range(qtdItens):
        qt, peso = input().split()
        item = {"qt": int(qt), "peso": int(peso)}
        lista.append(item)
        
    mochila(lista, 50, qtdItens)
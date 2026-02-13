
def mochila(projeteis: list[dict], k: int, hp: int) -> int:
    
    n = len(projeteis)
    matriz = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    
    for i in range(1,n + 1):
        poder = projeteis[i - 1].get("poder")
        peso = projeteis[i - 1].get("peso")
        
        for j in range(1, k + 1):
            item_anterior = matriz[i-1][j]
            poderAtual = -1
            
            if peso <= j:
                poderAtual = poder + matriz[i-1][j-peso]
            
            matriz[i][j] = max(poderAtual, item_anterior)


    if matriz[n][k] >= hp:
        print("Missao completada com sucesso")
    else:
        print("Falha na missao")


    return matriz[n][k]
    
N = int(input())

for _ in range(N):
    projeteis = []
    
    qtdBatalhoes = int(input())
    
    for _ in range(qtdBatalhoes):
        x, y = input().split()
        
        projeteis.append({"poder": int(x), "peso": int(y)})
    
    capacidade = int(input())
    
    hp = int(input())
    
    mochila(projeteis, capacidade, hp)
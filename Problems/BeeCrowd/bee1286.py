

def mochila(pizzas: list[dict], capacidade: int) -> int:

    n = len(pizzas)
    matriz = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    
    
    for i in range(1, n + 1):
        tempo = pizzas[i - 1].get("tempo")
        qtd = pizzas[i - 1].get("qtd")
    
    
        for j in range(1, capacidade + 1):
            tempo_anterior = matriz[i-1][j]
            tempo_atual = -1
            
            if qtd <= j:
                tempo_atual = tempo + matriz[i-1][j-qtd]
            
            matriz[i][j] = max(tempo_atual, tempo_anterior)
    
    return matriz[n][capacidade]


n = int(input())

while n != 0:
    
    capacidadeRoberto = int(input())
    pizzas = []
    
    for _ in range(n):
        tempo, qtd = input().split()
        
        pizzas.append({"tempo": int(tempo), "qtd": int(qtd)})
    
    
    print(f"{mochila(pizzas, capacidadeRoberto)} min.")
        


    n = int(input())
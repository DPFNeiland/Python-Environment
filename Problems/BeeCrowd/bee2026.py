

# p: numero de pacotes
# w: capacidade de peso suportado pela árvore
# e: numero de efeite de cada pacote
# pc: peso de cada pacote

def mochila(pacotes: list[dict], capacidade: int) -> int:
    n = len(pacotes)
    matriz = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        e = pacotes[i - 1].get("e")
        pc = pacotes[i - 1].get("pc")
        
        for j in range(1, capacidade + 1):
            item_anterior = matriz[i-1][j]
            enfeite_atual = -1
            
            if pc <= j:
                enfeite_atual = e + matriz[i-1][j-pc]
            
            matriz[i][j] = max(item_anterior, enfeite_atual)
    
    
    return matriz[n][capacidade]

g = int(input())

for i in range(1, g + 1):

    pacotes = []
    
    p = int(input())
    w = int(input())
    
    for _ in range(p):
        e, pc = input().split()
        
        pacotes.append({"e": int(e), "pc": int(pc)})
        
    print(f"Galho {i}:")
    print(f"Numero total de enfeites: {mochila(pacotes, w)}")
    print()
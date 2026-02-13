
# import sys
# c, f = map(int, sys.stdin.readline().split())

# c = int(c)
# f = int(f)

# cont = 0

# def mochila(mensagens: list[tuple], capacidade: int) -> int:
#     n = len(mensagens)
#     matriz = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    
#     for i in range(1, n+1):
#         qtdCaracteres = mensagens[i-1][0]
#         qtdDesculpas = mensagens[i-1][1]
        
#         for j in range(1, capacidade + 1):
#             desculpas_anterior = matriz[i-1][j]
#             desculpas_atual = -1
            
#             if qtdCaracteres <= j:
#                 desculpas_atual = qtdDesculpas + matriz[i-1][j-qtdCaracteres]
            
#             matriz[i][j] = max(desculpas_anterior, desculpas_atual)
    
#     return matriz[n][capacidade]

# while c != 0 and f != 0:
#     cont += 1
#     mensagens = []
    
#     for _ in range(f):
#         n, d = map(int, sys.stdin.readline().split())
        
#         mensagens.append((n,d))
    
    
#     print(f"Teste {cont}")
#     print(f"{mochila(mensagens, c)}")
#     print()
    
    
    
#     c, f = map(int, sys.stdin.readline().split())
import sys


def mochila(mensagens: list[tuple[int, int]], capacidade: int) -> int:

    dp = [0] * (capacidade + 1)
    

    for qtdCaracteres, qtdDesculpas in mensagens:
        for j in range(capacidade, qtdCaracteres - 1, -1):
            

            desculpas_anterior = dp[j] 
    
            desculpas_atual = qtdDesculpas + dp[j - qtdCaracteres]
            

            dp[j] = max(desculpas_anterior, desculpas_atual)
            
    return dp[capacidade]



cont = 0


def ler_cf():
    try:
        linha = sys.stdin.readline()
        if not linha:
            return 0, 0
        return map(int, linha.split())
    except:
        return 0, 0


c, f = ler_cf()

while c != 0 or f != 0:
    cont += 1
    mensagens = []
    
    for _ in range(f):
        try:
            n, d = map(int, sys.stdin.readline().split())
            mensagens.append((n, d))
        except:
            break
            
    
    print(f"Teste {cont}")
    print(mochila(mensagens, c))
    print()
    sys.stdout.flush() 
    

    c, f = ler_cf()
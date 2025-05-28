





while True:
    try:
        N = int(input())        
        
        matriz = [[3 for _ in range(N)] for _ in range(N)]
        
        for i in range(0, N):
            matriz[i].append(3)
        
        for i in range(0, N):            
            matriz[i][i] = 1
            
        for i in range(0, N):
            for j in range(0, N):
                if i + j == N - 1:
                    matriz[i][j] = 2
        
        for i in range(0, N):
            for j in range(0, N):
                print(matriz[i][j], end="")
                
            print()
        
        
    except EOFError:
        break
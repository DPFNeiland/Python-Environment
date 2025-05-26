




while True:
    try:
        N = int(input())        
        
        matriz = [[0 for _ in range(N)] for _ in range(N)]
        
        for i in range(0, N):
            matriz[i].append(0)
        
        print(matriz)
        
        
        for i in range(0, N):            
            matriz[i][i] = 2
            
        for i in range(0, N):
            for j in range(0, N):
                if i + j == N - 1:
                    matriz[i][j] = 3
        
        for i in range(0, N):
            for j in range(0, N):
                print(matriz[i][j], end="")
                
            print()
            
        if N % 2 == 1:
            matriz[N // 2][N // 2] = 4
        
        
    except EOFError:
        break
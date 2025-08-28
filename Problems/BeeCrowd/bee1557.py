
N = 1

while N != 0:
    N = int(input())
      
    matriz = [[
        2 ** (x+i) for x in range(N)] 
            for i in range(N)
              ]
    
    for i in range(0, N):
        for j in range(0, N):
            print(f"{matriz[i][j]:9}", end="")
        print()
    print()
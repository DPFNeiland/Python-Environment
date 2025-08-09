


N, M = input().split()

N = int(N)
M = int(M)

todos = []

matriz = [0 for j in range(N)]

for i in range(N):
    matriz[i] = list(map(int, input().split()))
matrizResposta = matriz
    
for i in range(N):
    for j in range(M):
        todos.append(matriz[i][j])
        
todos.sort()

print(todos)

for i in range(N):
    for j in range(M):
        indic = 0
        
        agrTem = 0        
        quantasTem = todos.count(matrizResposta[i][j])
        
        if matrizResposta[i][j] == todos[indic]:
            agrTem += 1
        
        print(matrizResposta[i][j])
        while matrizResposta[i][j] >= todos[indic] and agrTem < quantasTem:
            matrizResposta[i][j] += todos[indic]
            indic+=1
            print(matrizResposta[i][j])
            if indic >= len(todos):
                break
            
print(matrizResposta)
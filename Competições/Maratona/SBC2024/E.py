# Forma longa:



# Verifica se a matriz atende as condições da questão
# def Verificar_Matriz(m):
    
#     for i in range(N - 1):
#         for j in range(N - 1):
#             if m[i][j] >= m[i+1][j] or m[i][j] >= m[i][j+1]:
#                 return False
    
#     return True

# # Gira 90 graus a matriz anti-horário
# def Girar_Matriz(m):
#     aux = [[0 for _ in range(N)] for _ in range(N)] 
    
#     for i in range(N):
#         for j in range(N):
#                 aux[N - j - 1][i] = m[i][j]            
            

#     m = aux
#     return m
# N = int(input())
# resp = 0



# estojo = []

# for i in range(N):
#     estojo.append(list(map(int, input().split())))
    
# while not Verificar_Matriz(estojo):
#     estojo = Girar_Matriz(estojo)
#     resp += 1
    
# print(resp)

# Forma curta:
N = int(input())
estojo = []
resp = 0

for i in range(N):
    estojo.append(list(map(int, input().split())))

importante = [estojo[0][0], estojo[0][ N - 1], estojo[ N - 1][ N - 1], estojo[ N - 1][0] ]
menor = importante[0]

for i in range(4):
    if menor > importante[i]:
        resp = i
        menor = importante[i]
         
print(resp)
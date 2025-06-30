

def add_edge(mat, i,j):
    
    mat[i][j] = 1
    mat[j][i] = 1
    # o grafo não é unidirecional

def display_matriz(mat):
    
    for row in mat:
        print("".join(map(str,row)))
        
        
V = 4
mat = [[0] * V for _ in range(V)]

add_edge(mat,0,1)
add_edge(mat,0,2)
add_edge(mat,1,2)
add_edge(mat,2,3)

display_matriz(mat)

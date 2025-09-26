

def multMatriz(a: list, b: list) -> list:
    
    c = []    
    for i in range(len(a)):
        
        linha = []
        for j in range(len(b[0])):
            soma = 0
            for k in range(len(a[i])):    
                soma += a[i][k]*b[k][j]
                
            linha.append(soma)
        c.append(linha)
        
    return c
  
# 5 2 7
# 3 0 3
# 4 1 5

def main():
    matriz1 = [[1, 2], [3, 0], [2, 1]]
    matriz2 = [[1, 0, 1], [2, 1, 3]]

    c = multMatriz(matriz1, matriz2)
    print(c)
    
if __name__ == "__main__":
    main()
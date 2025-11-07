

def subsequencia(palavra1: str, palavra2: str):
    
    p1 = len(palavra1)  
    p2 = len(palavra2)
    
    matriz = [[0 for _ in range(p2 + 1)] for _ in range(p1 + 1)]
        
    for i in range(1, p1 + 1):
        for j in range(1, p2 + 1):
            if palavra1[i - 1] == palavra2[j - 1]:
                matriz[i][j] = 1 + matriz[i -1 ][j - 1] 

            else:
                matriz[i][j] = max(matriz[i-1][j],matriz[i][j-1])
            
    print(matriz[p1][p2])

def main():
    palavra1 = input()
    palavra2 = input()
    
    
    subsequencia(palavra1, palavra2)
    
    
if __name__ == "__main__":
    main()
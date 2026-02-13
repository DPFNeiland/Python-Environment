

N = int(input())

for j in range(0, N):
    
    notas = list(map(int, input().split()))

    acimaMedia = 0
    soma = 0
    
    for i in range(1, len(notas)):
        soma += notas[i]
        
    for i in range(1, len(notas)):
        if notas[i] > soma/notas[0]:
            acimaMedia += 1
            
            
    print(f'{acimaMedia/notas[0]*100:.3f}%')
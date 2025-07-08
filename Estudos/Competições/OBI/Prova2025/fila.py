

N = int(input())

cadeira = list(map(int,input().split()))
tamanho = len(cadeira)
resp = 0
maior = cadeira[tamanho - 1] 

if (N == 1):
    resp = 0

elif tamanho - 1 == 1:

    if(cadeira[1] >= cadeira[0]):
        resp = 1
    else:
        resp = 0
else:
    cadeira.pop()
    tamanho = len(cadeira)
    
    for i in range(tamanho - 1, -1, -1):

        if maior >= cadeira[i]:
            resp += 1
        else:
            maior = cadeira[i]
            
print(resp)




n = int(input())

lista = []

soma = 0

for i in range(n):
    
    x = int(input())
    
    if x != 0:
        lista.append(x)
        soma += x
        
    else:
        soma -= lista.pop()
        
print(soma)
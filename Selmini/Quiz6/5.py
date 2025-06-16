

a = 5
b = 55
c = 555


maior = a
menor = 0

if maior > b:
    maior = b
    
else:
    if maior > c:
        maior = c
        menor = c
        
    if menor < a:
        menor = a
    else:
        if menor < b:
            menor = b
            
outro = a + b + c - maior - menor

print(maior)
print(menor)
print(outro)
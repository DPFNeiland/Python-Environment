
i = 0
soma = 0
valores = []

while i < 3:
    resp = input()
    
    
    if resp != "caw caw":
        if resp[0] == "*":
            soma += 4
        
        if resp[1] == "*":
            soma += 2
            
        if resp[2] == "*":
            soma += 1
    else:
        valores.append(soma)
        soma = 0
        i += 1
        
for i in valores:
    print(i)
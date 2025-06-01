


bal = input("")

duplicado = [False, False, False, False]
num = 0

# Copas, Espadas, Ouros e Paus (C, E, U, P)

Copas = []
Espadas = []
Ouros = []
Paus = []

restantes = [13,13,13,13]

for i in range(0, len(bal)):
    if i % 3 == 0:
        num += (int(bal[i])*10)    
    
    if i % 3 == 1:
        num += int(bal[i])
        
    if i % 3 == 2:
        naipe = bal[i]
        
        if naipe == 'C':
            if Copas.count(num) >= 1:
                duplicado[0] = True
                
            else:
                Copas.append(num)
                restantes[0] -= 1
                num = 0
     
     
        if naipe == 'E':
            if Espadas.count(num) == 1:
                duplicado[1] = True

                
            else:
                Espadas.append(num)
                restantes[1] -= 1       
                num = 0
                
                
        if naipe == 'U':
            if Ouros.count(num) >= 1:
                duplicado[2] = True
                
            else:
                Ouros.append(num)
                restantes[2] -= 1     
                num = 0      
                
                
        if naipe == 'P':
            if Paus.count(num) >= 1:
                duplicado[3] = True
                
            else:
                Paus.append(num)
                restantes[3] -= 1    
                num = 0
                
        num = 0
                
for i in range(4):                
    print(f'{"erro" if duplicado[i] else restantes[i]}')


# Copas, Espadas, Ouros e Paus (C, E, U, P)

# 01C 02C 03C 04C 05C 07C 09C 10C 11C 02E 02E 03E 11U


bal = input()

duplicado = [False, False, False, False]
num = 0

Copas = []
Espadas = []
Ouros = []
Paus = []

restantes = [13, 13, 13, 13]

for i in range(0, len(bal)):
    if i % 3 == 0:
        num = int(bal[i]) * 10

    if i % 3 == 1:
        num += int(bal[i])

    if i % 3 == 2:
        naipe = bal[i]

        if naipe == 'C':
            if num in Copas:
                duplicado[0] = True
            else:
                Copas.append(num)
                restantes[0] -= 1

        if naipe == 'E':
            if num in Espadas:
                duplicado[1] = True
            else:
                Espadas.append(num)
                restantes[1] -= 1

        if naipe == 'U':
            if num in Ouros:
                duplicado[2] = True
            else:
                Ouros.append(num)
                restantes[2] -= 1

        if naipe == 'P':
            if num in Paus:
                duplicado[3] = True
            else:
                Paus.append(num)
                restantes[3] -= 1

        num = 0  # zera ao final do processamento da carta

for i in range(4):
    print("erro" if duplicado[i] else restantes[i])

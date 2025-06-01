

placa = input()

ehPlaca = 0

if len(placa) == 8:
    for i in range(0, len(placa)):
        if (placa[i] >= 'A' and placa[i] <= 'Z' ) and (i == 0 or i == 1 or i == 2):
            ehPlaca = 1

        if (i == 4 and placa[i] == '-'):
            ehPlaca = 1
        
        if (i == 5 or i == 6 or i == 7 or i == 8) and (placa[i] >= '0' and placa[i] <= '9'):
            ehPlaca = 1
            
if len(placa) == 7:
    for i in range(0, len(placa)):
        if (placa[i] >= 'A' and placa[i] <= 'Z' ) and (i == 0 or i == 1 or i == 2 or i == 4):
            ehPlaca = 2
        
        if (i == 3 or i == 5 or i == 6) and (placa[i] >= '0' and placa[i] <= '9'):
            ehPlaca = 2   

print(ehPlaca)
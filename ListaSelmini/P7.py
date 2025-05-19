



N = int(input("Digite um número: "))

# n = 55

# 55 < 9 = False

# 55 < 99 = True

# 2 dígitos

if N == 0 :
    print("1 dígito")
    
elif N > 0:
    
    contadora = 1
    
    while True:
        
        if N <= 10 ** contadora - 1: # if N <= pow(10,2) - 1
            resposta = contadora
            break
        
        contadora += 1    
        
    print(f"O número tem {contadora} dígitos")
    
else:
    
    contadora = 1
    
    while True:
        
        if N >= (10 ** contadora - 1) * -1:
            resposta = contadora
            break
        
        contadora += 1    
        
    print(f"O número tem {contadora} dígitos")
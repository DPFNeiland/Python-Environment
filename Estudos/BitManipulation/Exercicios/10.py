

def Contar_Bits(numero):
    BITS = 31
    
    cont = 0
    for i in range(BITS):
        if (1 << i) & numero:
            cont += 1
            
    return cont

N = int(input())

print(Contar_Bits(N))
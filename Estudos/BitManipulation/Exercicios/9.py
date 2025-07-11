

def Contar_Bits(numero):
    BITS = 31
    qtdBits = 0
    for i in range(BITS):
        if (1 << i) & numero:
            qtdBits +=1
        
    return qtdBits

def Maior_M_possivel(numero, cont):
    # também pode usar o bit_count()
    while cont != Contar_Bits(numero):
        numero +=1
    
    return numero
    
    
    
N, K = [int(x) for x in input().split()]

print(Maior_M_possivel(N, K))
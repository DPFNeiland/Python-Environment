

def Verificar_Bit_Valido(n):
    
    for i in range(BITS, -1, -1):
        if (1 << i) & n:
            return i
    
    return -1

BITS = 31
N = int(input())

print(Verificar_Bit_Valido(N))


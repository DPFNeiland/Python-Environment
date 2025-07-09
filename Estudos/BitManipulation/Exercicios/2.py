
def Contar_Bits(n):
    
    cont = 0
    for i in range(31):
        if (1 << i) & n:
            cont += 1
            
    return cont

N = int(input())

print(Contar_Bits(N))

# Tudo certo
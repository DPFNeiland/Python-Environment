
def Contar_Bits(conjunto):
    cont = 0
    BITS = 31
    
    for i in range(BITS):
        if (1 << i) & conjunto:
            cont += 1
    
    return cont
    
def Calcular_Fatorial(n):
    if n <= 1:
        return 1
    
    return n*Calcular_Fatorial(n-1)
# Tomar cuidado com isso, porque dependendo do n, pode estourar a função toda

def Calcular_SubConjuntos(a,b) :
    
    if a < 0 or a < 0 or a - b < 0:
        return 0 
    else:
        return int(Calcular_Fatorial(a)/(Calcular_Fatorial(b)*Calcular_Fatorial(a-b)))
          

A, K = [int(x) for x in input().split()]

print(Calcular_SubConjuntos(Contar_Bits(A),K))



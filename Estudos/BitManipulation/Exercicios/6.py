BITS = 31

def Conferir_SubConjunto(ConjA, ConjB):
    
    for i in range(BITS):
        if ((1 << i) & ConjA) and not((1 << i) & ConjB):
            return False
        
    return True

A, B = [int(x) for x in input().split()]

print("SIM" if Conferir_SubConjunto(A, B) else "NÃO")

# Ou também (A & B) == A

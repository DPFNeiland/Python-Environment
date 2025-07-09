
BITS = 31

A, B = [int(x) for x in input().split()]

X = A & B

cont = 0
for i in range(BITS):
    if (1 << i) & X:
        cont += 1
    
print(cont)
        

# Tudo Certo
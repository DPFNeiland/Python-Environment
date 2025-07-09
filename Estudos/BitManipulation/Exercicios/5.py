
BITS = 31

A = int(input())

for i in range(BITS):
    if (1 << i) & A:
        print(i)
        break
    
# Tudo certo

A, x = input().split()
A = int(A)
x = int(x)

print("SIM" if (1 << x) & A else "NÃO")

# Tudo certo
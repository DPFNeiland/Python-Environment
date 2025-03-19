


L, D = [float(x) for x in input().split()]
K, P = [float(x) for x in input().split()]

aux = L*K

while(L-D>=0):
    L = L - D
    aux = aux + P

print(f'{aux:.0f}')
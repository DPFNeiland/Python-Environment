

E = int(input())
S = int(input())
L = int(input())

resp = 0

if E > S and E > L:
    resp = 2*(E - min(L,S)) 
    
elif E < S and E < L:
    resp = 2*(max(L,S) - E)
else:
    resp = 2*((max(L,S) - E) + (E-min(L,S)))
print(resp)
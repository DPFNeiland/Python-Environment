

def muitoFeio(x, v, n):
    if n == 0: return 0
    feio = muitoFeio(x, v, n - 1)
    if feio == 1 or x == v[n - 1]: return 1
    
print(muitoFeio(9, [5,3,2,11,9,10],6))
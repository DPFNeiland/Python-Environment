def TransformarCharPraInt(c):
    return ord(c) - ord('0')

def CalcularResto(s: str, d: int) -> int:
    base = 1 % d
    res = 0
    
    for i in range(len(s) -1, -1, -1):
        digito = TransformarCharPraInt(s[i])
    
        res = (res + (digito*base)%d)%d
        
        base = (base*10) % d
    
    return res

N = input()

if CalcularResto(N, 2) == 0:
    print('S')
else:
    print('N')

if CalcularResto(N, 3) == 0:
    print('S')
else:
    print('N')

if CalcularResto(N, 5) == 0:
    print('S')
else:
    print('N')

def TransformarCharParaInt(c: str):
    return ord(c) - ord('0')

def CalcularResto(s: str, d: int) -> int:
    base = 1%d
    res = 0
    
    for i in range(len(s)-1,-1,-1):
        
        num = TransformarCharParaInt(s[i])
        res = (res + (num*base)%d)%d
        base = (base*10)%d
        
    return res

N = input()

if CalcularResto(N, 11) == 0:
    print("S")
else:
    print("N")
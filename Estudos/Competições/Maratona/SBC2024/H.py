

def TransformarCharParaInt(c: str):
    return ord(c) - ord('0')
    
def RetornarResto(s: str, d: int) -> int:
    base = 1%d
    res = 0
    
    for i in range(len(s) - 1, -1, -1):
        num = TransformarCharParaInt(s[i])
        
        res = (res + (num*base)%d)%d
        
        base = (base*10)%d

    return res



M = input()
N = input()

temAsteriscoNoN = False
for carac in N:
    if carac == "*":
        temAsteriscoNoN = True
        break
    
if not temAsteriscoNoN:
    sum = 0
    for i in range(len(N)-1,-1,-1):
        sum += int(N[i])*2**(i)
 
 
        
temAsteriscoNoM = False
for carac in M:
    if carac == "*":
        temAsteriscoNoM = True
        break
    
if not temAsteriscoNoM:
    sum = 0
    for i in range(len(M)-1,-1,-1):
        sum += int(M[i])*2**(i)




def Transformar_Char_Pra_Int(c: str):
    return ord(c) - ord('0')


def Calcular_Resto(s: str, d: int):
    base = 1%d
    resto = 0
    
    for i in range(len(s) -1, -1, -1):
        num = Transformar_Char_Pra_Int(s[i])
        
        resto = (resto + (num*base)%d)%d
        
        base = (base*10)%d
        
    return resto

N = input()

if Calcular_Resto(N, 4) == 0:
    print("S")
else:
    print("N")
    
if Calcular_Resto(N, 9) == 0:
    print("S")
else:
    print("N")
    
if Calcular_Resto(N, 25) == 0:
    print("S")
else:
    print("N")
    

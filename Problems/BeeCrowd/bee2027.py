
def GDCsimp(num: int, den: int):
    
    if den > 0:
        return GDCsimp(den, num%den)
    
    return num

aposta = [0] * 100
cont = -1

while True:
    try:
        num, den = map(int, input().split())
        cont += 1
        
        aposta[cont] = GDCsimp(num, den)
        
        if aposta[cont] <= 5 :
            print("Gnomos")
        else:
            print("Noel")

        
    except EOFError:
        break
    
for i in range(cont, -1, -1):
    print(aposta[i], end=" ") 
    
print()
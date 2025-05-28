

while True:
    try:
        L = int(input())
        
        
        velocidadeLesmas = list(map(int, input().split()))
        
        vMax = -1
        for velocidades in velocidadeLesmas:
            if velocidades < 10:
                vMax = max(vMax, 1)
            elif velocidades >= 10 and velocidades < 20:
                vMax = max(vMax,2)
            else:
                vMax = max(vMax,3)
                            
        print(vMax)
    except EOFError:
        break
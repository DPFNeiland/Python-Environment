
while (True):
    try:
        D, VF, VG = [float(x) for x in input().split(' ')]
        
        D = float(D)
        VF = float(VF)
        VG = float(VG)
        
        disguard = (12 ** 2 + D ** 2) ** (1/2)
        
        if disguard / VG <= 12 / VF:
            print('S')
        else:
            print('N')
        
    except EOFError:
        break

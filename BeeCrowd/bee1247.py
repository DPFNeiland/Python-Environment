
while (True):
    try:
        D, VF, VG = [float(x) for x in input().split(' ')]
        
        D = float(D)
        VF = float(VF)
        VG = float(VG)
        
        if(VF == VG):
            resp = str('N')
            print(resp)
        elif((VG + D)*(VG - D)> 144 or (VG + D)*(VG - D) < 0):
            resp = str('N')
            print(resp)
        else:
            resp = str('S')
            print(resp)
        
    except EOFError:
        break

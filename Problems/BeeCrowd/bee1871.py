

Ni = 1
Mi = 1

while Ni != 0 and Mi != 0:
    Ni, Mi = [int(x) for x in input().split()]

    if Ni != 0 and Mi != 0:
        
        Resp = str(int(Ni) + int(Mi))

        for i in range(0,12):
            Resp = Resp.replace("0","")
            
        
        
        print(f'{Resp}')        
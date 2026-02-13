
N = 1

while N != 0:
    N = int(input())

    for i in range(0,N):
        Aresp, Bresp, Cresp, Dresp, Eresp = False, False, False, False, False
        resp = 0
        A, B, C, D, E = [int(x) for x in input().split()]
        
        
        if(A <= 127):
            Aresp = True
            resp += 1
            
        if(B <= 127):
            Bresp = True
            resp += 1
        
        if(C <= 127):
            Cresp = True
            resp += 1
            
        if(D <= 127):
            Dresp = True
            resp += 1
            
        if(E <= 127):
            Eresp = True
            resp += 1
        
        if(resp > 1):
            print('*')
            
        elif Aresp:
            print('A')
        
        elif Bresp:
            print('B')
            
        elif Cresp:
            print('C')
            
        elif Dresp:
            print('D')
            
        elif Eresp:
            print('E')
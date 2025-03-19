

import math

while True:
    try:
        h = float(input())
        p1, p2 = input().split()

        p1 = float(p1)
        p2 = float(p2)

        n = int(input())

        g = 9.80665

    
        for i in range(0,n):
        
            alpha, Vel = input().split()
            alpha = float(alpha)*3.14159/180
            Vel = float(Vel)
    

            t = (Vel*math.sin(alpha) + math.sqrt(2*h*g + (Vel*math.sin(alpha))**2))/g

            if Vel*math.cos(alpha)*t >= p1 and Vel*math.cos(alpha)*t <= p2:
                print(f"{Vel*math.cos(alpha)*t:.5f} -> DUCK")
            else:
                print(f"{Vel*math.cos(alpha)*t:.5f} -> NUCK")
    except EOFError:
            break        



x1, y1 = [float(i) for i in input().split()]
x2, y2 = [float(i) for i in input().split()]
x3, y3 = [float(i) for i in input().split()]
x4, y4 = [float(i) for i in input().split()]

N = int(input())

DisMax = -1.0

for i in range(0,N):
    x, y = [float(i) for i in input().split()]
    
    if(((x1-x)**2+(y1-y)**2)**(1/2) >= DisMax):
        DisMax = ((x1-x)**2+(y1-y)**2)**(1/2)
        
    elif(((x2-x)**2+(y2-y)**2)**(1/2) >= DisMax):
        DisMax = ((x2-x)**2+(y2-y)**2)**(1/2)
    
    elif(((x3-x)**2+(y3-y)**2)**(1/2) >= DisMax):
        DisMax = ((x3-x)**2+(y3-y)**2)**(1/2) 
    
    elif(((x4-x)**2+(y4-y)**2)**(1/2) >= DisMax):
        DisMax = ((x4-x)**2+(y4-y)**2)**(1/2)
    
print(f'{DisMax:.11f}')
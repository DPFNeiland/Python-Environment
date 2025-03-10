
'''
X1 = float(input(" Digite a coordenada X do primeiro ponto: "))
Y1 = float(input(" Digite a coordenada Y do primeiro ponto: "))

X2 = float(input(" Digite a coordenada X do segundo ponto: "))
Y2 = float(input(" Digite a coordenada Y do primeiro ponto: "))
'''

X1, Y1 = ([float(x) for x in input().split(" ")])

X2, Y2 = ([float(x) for x in input().split(" ")])

distancia1 = ((X1)**2+(Y1)**2)**(1/2)

distancia2 = ((X2)**2+(Y2)**2)**(1/2)

if(distancia1 > distancia2):
    print(f"Os pontos ({X2:.2f},{Y2:.2f}) são os mais próximos da origem")
elif(distancia2>distancia1):
    print(f"Os pontos ({X1:.2f},{Y1:.2f}) são os mais próximos da origem")
else:
    print(f"Os pontos ({X1:.2f},{Y1:.2f}) e ({X2:.2f},{Y2:.2f}) são equidistantes em relação a origem")
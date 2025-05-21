
from math import inf

max = -inf
min = inf

xMax = 0
xMin = 0

yMax = 0
yMin = 0

qtd = int(input("Qual a quantidade de pontos que serão informados? --> "))


for i in range(0,qtd): 
    print(f'Ponto {i+1}')
    x = float(input("x --> "))
    y = float(input("y --> "))
    dist = (x**2 + y**2) ** (1/2)
    print(f'Distância até a origem --> {dist:.4f}', end="\n\n")
    
    if dist < min:
        min = dist
        xMin = x
        yMin = y
        
    if dist > max:
        max = dist
        xMax = x
        yMax = y
        
print(f"O ponto mais distante tem coordenadas --> ({xMax:.2f}, {yMax:.2f})", end="\n\n")
print(f"O ponto mais perto tem coordenadas --> ({xMin:.2f}, {yMin:.2f})")
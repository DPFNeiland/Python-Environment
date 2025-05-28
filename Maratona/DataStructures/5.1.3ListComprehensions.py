

squares = []

for x in range(10):
    squares.append(x**2)

squares = list(map(lambda x: x**2, range(10)))

squares = [x ** 2 for x in range(10)]

print(squares)


print([(x,y) for x in [1,2,3] for y in [3, 1, 4] if x != y]) 
  
combs = []


for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

print(combs)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]



vec = [-4, -2, 0, 2, 4]

print([x*2 for x in vec]) # [-8, -4, 0, 4, 8]

print([x for x in vec if x >= 0]) # [0, 2, 4]

print([abs(x) for x in vec]) # [4, 2, 0, 2, 4]

freshfruit = [' banana', ' loganberry ', 'passion fruit  ']

print([weapon.strip() for weapon in freshfruit])

print([(x, x**2) for x in range(6)])

# Tem que ter o parentese


vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

from math import pi

print([str(round(pi,i)) for i in range(1,6)])

class Ponto:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
def mover(p: Ponto, dx: float, dy: float) -> Ponto:
    p.x += dx
    p.y += dy
    return p

p1 = Ponto(1, 2)
p2 = p1
p3 = mover(p2, 3, -1)
print(p1.x)
print(p1.y)
print(p2.x)
print(p2.y)
print(p3.x)
print(p3.y)
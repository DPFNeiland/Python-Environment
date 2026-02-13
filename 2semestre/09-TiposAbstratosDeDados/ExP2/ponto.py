import math

class Ponto:
    # construtor
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def calcular_distancia(self, p: "Ponto") -> float:
        return math.hypot(self.x - p.x, self.y - p.y)
    
    def calcular_distancia_da_origem(self) -> float:
        return math.hypot(self.x, self.y)
    
    # sobreposição de método ou override        
    def __str__(self):
        return f'{self.x}, {self.y}'
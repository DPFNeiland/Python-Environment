class Ponto:

    # construtor
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def calcular_distancia(self, xi: float = 0.0, yi : float = 0.0) -> float:
        return ((self.x - xi) ** 2 + (self.y - yi) ** 2) ** (1/2)
    
    def imprimir_Ponto(self) -> tuple:
        return (self.x, self.y)
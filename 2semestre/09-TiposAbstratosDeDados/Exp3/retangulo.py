import math
from ponto import Ponto

class Retangulo:
    # construtor
    def __init__(self, largura: float, altura: float, canto_superior_esquerdo: Ponto):
        self.largura = largura
        self.altura = altura
        self.canto_superior_esquerdo = canto_superior_esquerdo

    def calcular_area(self) -> float:
        return self.altura * self.largura
    
    def calcular_perimetro(self) -> float:
        return 2 * (self.altura + self.largura)
    
    # sobreposição de método ou override        
    def aumentar_tamanho(self, altura: float, largura: float) -> float:
        self.largura += largura
        self.altura += altura

    def coordenada_centro(self) -> Ponto:
        xc = self.canto_superior_esquerdo.x + self.largura/2
        yc = self.canto_superior_esquerdo.y - self.altura/2
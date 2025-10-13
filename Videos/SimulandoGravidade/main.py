# Simular a força da gravidade

import cv2
import numpy as np

def RodarQueda(ambiente, orig_ambiente,  X: int, Y: int):
    
    ambiente = orig_ambiente.copy()
    CriarAmbiente(ambiente)
    CriarObjeto(ambiente, X, Y)

    cv2.imshow("Mundo", ambiente)   

    
def CriarObjeto(ambiente, X, Y):
    cv2.circle(ambiente, (X, Y), 10, (201, 87, 40), -1)     

def CriarAmbiente(ambiente):
    ### desenhar os objetos do mundo

    # desenhar o retângulo vertical
    cv2.rectangle(ambiente, (0,20), (20,290), (10,30,50), -1)
    
    # retangulo horizontal
    cv2.rectangle(ambiente, (0,290), (300,300), (10,30,50), -1)

# processamento
def movimentarBola(t):
    # S = S0  +V0t - 0.5at² (S0 = 0m, V0 = 0 m/s, a = g ≈ 10 m / s²) = S = -0,5t²
    
    Ponto = []
    x = 30
    S = 0
    S0 = 0
    S = 5*t*t # S é justamente a altura da bola? Ponto central da bola = P(X,Y) = P(30,S)
    y = S + 20
    
    P = x, y     
    return P


def main():
    # desenhar o ambiente (mundo)
    ambiente = np.full((300,300,3), (0,100,0),dtype=np.uint8)

    
    
    orig_ambiente = ambiente.copy()
    CriarAmbiente(ambiente)

    for tempo in range(10):
        ponto = movimentarBola(tempo) # (x, y)
        print(ponto)
        
        if ponto[1] > 280:
            RodarQueda(ambiente, orig_ambiente, 30, 280)
                     
            break
        
        RodarQueda(ambiente, orig_ambiente, 30, ponto[1])
        
        cv2.waitKey(500)
        
    
    
    while True:
        print("clicou")
        cv2.waitKey(0)


if __name__ == '__main__':
    main()
import random
ponto = list[float]

def gerar_dados(k = 9):

        # [1.0, 1.0], [1.2, 0.9], [0.9, 1.1], # Grupo A
        # [4.0, 4.2], [3.9, 3.5], [4.1, 3.8], # Grupo B
        # [8.0, 8.0], [8.3, 7.9], [7.7, 8.2]  # Grupo C
        
    
    dados = []

    for i in range(k):
        dados.append([random.randint(0, k**2)/10, random.randint(0, k**2)/10])

    return dados


def kmeans(dados: list[ponto], k: int, max_iter: int = 200, tolerancia: float = 1e-6):
    n = len(dados) # tamanho da lista
    dimensao = len(dados[0]) # número de elementos em cada lista

    indices = list(range(n))
    random.shuffle(indices)

    centros = [dados[indices[i]][:] for i in range(k)]

    it = 1
    while it <= max_iter:
        for i in range(n):
            dado = dados[i]
            menor_distancia = float('inf')
            for j in range(k):
                 dist = distancia(dado, centros[j])
                 if dist < menor_distancia:
                     menor_distancia = dist

    
def distancia(dado, centros):

    return ((dado[0] - centros[0])**2 +(dado[0] - centros[0])**2)**(1/2)



def main():
    dados = gerar_dados(9)
    print(dados)

    kmeans(dados, k = 3, max_iter = 200, tolerancia = 1e-6)

if __name__ == "__main__":
    main()
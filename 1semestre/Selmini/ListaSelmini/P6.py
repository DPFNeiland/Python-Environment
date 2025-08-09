

from math import inf


n = int(input("Digite o número de competidores: "))

nomeVencedor = "Ninguem"

distancia1 = inf
distancia2 = inf

for i in range(0, n):
    
    nomeDoCandidato = input(f"Digite o nome do {i + 1}º candidato: ")

    tentativa1 = int(input(f"Digite a distância em metros adquirida pelo candidato na primeira tentativa:"))
    tentativa2 = int(input(f"Digite a distância em metros adquirida pelo candidato na segunda tentativa:"))

    if distancia1 > tentativa1 and distancia2 > tentativa2:
        nomeVencedor = nomeDoCandidato
        distancia1 = tentativa1
        distancia2 = tentativa2
    
    if distancia1 > tentativa1 and distancia2 < tentativa2:
        nomeVencedor = "Ninguem"
        distancia1 = tentativa1
        distancia2 = tentativa2

    if distancia1 < tentativa1 and distancia2 > tentativa2:
        nomeVencedor = "Ninguem"
        distancia1 = tentativa1
        distancia2 = tentativa2



if nomeVencedor == "Ninguem":
    print("O torneio não teve um vencedor definido")

else: 
    print(f"O vencedor é {nomeVencedor} com as distâncias {distancia1} metros e {distancia2}")



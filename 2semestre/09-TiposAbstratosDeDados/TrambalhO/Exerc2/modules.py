from Rota import Rota
from typing import List
from random import randint

# Escreva um programa de teste que faça a leitura dos dados via terminal, gere objetos do tipo Rota e 
# armazene em uma lista. Em seguida, imprima as seguintes informações: 

def validar_input_float(variavel, texto) -> float:

    variavel = 0
    
    while variavel <= 0:
        variavel = float(input(texto))

    return variavel


def validar_input_int(variavel, texto) -> int:

    variavel = 0
    
    while variavel <= 0:
        variavel = int(input(texto))

    return variavel


def cadastrar_rotas() -> List:
    rotas = []

    qtdRotas = -1
    RotaNome = ""

    RotaTrechos = []


    qtdRotas = validar_input_int(qtdRotas, "Quantas rotas você quer cadastrar: ")

    print("-" * 75)

    for _ in range(qtdRotas):
        RotaNome = str(input("Digite o nome da rota: "))

        RotaTrechos = cadastrar_trechos()

        rotas.append(
            Rota(
                RotaNome,
                RotaTrechos
            )
        )

        print("-" * 75)

    return rotas


def cadastrar_trechos() -> List:

    RotaTrechos = []
    qtdTrechos = -1
    RotaRechoDist_km = -1.0
    RotaTrechoVel_kmh = -1.0
    RotaTrechoSemaforos = -1

    qtdTrechos = validar_input_int(qtdTrechos, "Quantos trechos da rota você quer cadastrar: ")

    for _ in range(qtdTrechos):
        print("-" * 50)

        RotaRechoDist_km = validar_input_float(
            RotaRechoDist_km, 
            "Digite a distância do trecho em quilômetros: "
        )
        
        RotaTrechoVel_kmh = validar_input_float(
            RotaTrechoVel_kmh, 
            "Digite a velocidade do trecho em quilômetros por hora: "
        )

        RotaTrechoSemaforos = validar_input_int(
            RotaTrechoSemaforos,
            "Digite o número de semáforos do trecho: "
        )
        RotaTrecho = {
            "dist_km": RotaRechoDist_km,
            "vel_kmh": RotaTrechoVel_kmh,
            "semaforos": RotaTrechoSemaforos
        }
        RotaTrechos.append(RotaTrecho)

    return RotaTrechos

# d) (1,5) calcule o tempo_total_min() para todas as rotas. Ordene da mais rápida para a mais lenta e 
# mostre um ranking. Você deverá utilizar um dos algoritmos de ordenação implementados em 
# aula. 
def quicksort(lista: list[Rota], inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
        
    if inicio < fim:
        pivo = particionar(lista, inicio, fim)
        quicksort(lista, inicio, pivo - 1.0)
        quicksort(lista, pivo + 1.0, fim)

def particionar(lista: List[Rota], inicio: int, fim: int) -> int:
    k = randint(inicio, fim)
    lista[k], lista[fim] = lista[fim], lista[k]
    
    pivo = lista[fim].tempo_total_min()
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j].tempo_total_min() <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1


def imprimir_rotas(Rotas: List[Rota]) -> None:

    quicksort(Rotas)
    print("-" * 50)
    print("[Ranking port Tempo Total]")
    print("Nome da Rota | Tempo (min) | Velocidade média (km/h) ")
    for rota in Rotas:
        
        print(f"{rota.nome:<13}", end="| ")
        print(f"{str(rota.tempo_total_min()) + " min":<11}", end=" | ")
        print(f"{str(rota.calcular_velocidade_media()):<20}")

# e) (1,5) Entre com os dados de uma janela de tempo (ex.: [35, 50] min) e liste todas as rotas que 
# atendem a janela. Os dados da janela deverão ser informados via terminal. 
def verificar_rotas_janela(Rotas: List[Rota]) -> None:

    inicio_min = -1
    fim_min = - 1

    inicio_min = validar_input_float(
        inicio_min,
        "Digite o início do intervalo: "
    )

    fim_min = validar_input_float(
        fim_min,
        "Digite o fim do intervalo: "
    )
    print("-" * 50)
    print(f"[Rotas que atendem a janela {inicio_min:.2f} min–{fim_min:.2f} min] ")
    print("Nome da Rota | Tempo (minutos)")
    for rota in Rotas:

        if rota.verificar_atende_janela(inicio_min, fim_min):

            print(f"{rota.nome:<13}", end="| ")
            print(f"{str(rota.tempo_total_min()) + " min"}")


# f) (1,5) Para todas as rotas, calcule vel_media_kmh() e custo_emissao(kg_co2_km) usando, por 
# exemplo, 0,192 kg CO₂/km. Exiba um quadro comparativo
def calcular_co2_rotas(Rotas: List[Rota]):
    constante_de_emissao_media = 0.192 
    
    print("-" * 50)
    print("[Comparativo de Emissões]")
    print("Nome da Rota | Distância (km) | Emissão (em kg*CO2) ")
    for rota in Rotas:
        distancia = rota.tempo_total_min()*rota.calcular_velocidade_media()/60 
        print(f"{rota.nome:<13}", end="| ")
        print(f"{str(int(distancia*100)/100) + " km":<14}", end=" | ")
        print(f"{str(int(rota.calcular_custo_emissao(constante_de_emissao_media)*1000)/1000) + " kg*CO2":<20}")
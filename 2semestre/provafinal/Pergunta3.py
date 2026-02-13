from random import randint

# Os objetos do tipo Sensor contém os seguinte atributos: código e leitura.
class Sensor:
    def __init__(self, codigo: int, leitura: float):
        self.codigo = codigo
        self.leitura = leitura

def CadastrarSensores() -> list:
    Sensores = list()

    n = int(input("Digite a quantidade de Leituras: "))

    for _ in range(n):
        print("-" * 50)
        SensorCodigo = int(input("Digite o id (inteiro): "))
        SensorLeitura = float(input("Digite o tipo da leitura: "))

        Sensores.append(
            Sensor(
                SensorCodigo,
                SensorLeitura,
            )
        )
    return Sensores


def ImprimirSensores(Sensores: list[Sensor]) -> list:

    print(f"ID     | Leitura [Em ordem crescente]")
    print("-" * 50)
    for sensor in Sensores:
        print(f"{sensor.codigo:<7}",end="| ")
        print(f"{sensor.leitura:<15}")

# Escreva uma função que receba como parâmetro uma lista contendo objetos do tipo Sensor
# A função deverá ordenar a lista de sensores em ordem crescente de leitura.
def quicksort(Sensores: list[Sensor], inicio = 0, fim = None):
    if fim is None:
        fim = len(Sensores) - 1
        
    if inicio < fim:
        pivo = particionar(Sensores, inicio, fim)
        quicksort(Sensores, inicio, pivo - 1)
        quicksort(Sensores, pivo + 1, fim)




def particionar(Sensores: list[Sensor], inicio: int, fim: int) -> int:
    k = randint(inicio, fim)
    Sensores[k], Sensores[fim] = Sensores[fim], Sensores[k]
    
    pivo = Sensores[fim].leitura
    i = inicio - 1
    
    for j in range(inicio, fim):
        if Sensores[j].leitura <= pivo:
            i += 1
            Sensores[i], Sensores[j] = Sensores[j], Sensores[i]

    Sensores[i + 1], Sensores[fim] = Sensores[fim], Sensores[i + 1]
    return i + 1

def main():
    Sensores = CadastrarSensores()
    quicksort(Sensores)

    ImprimirSensores(Sensores)

if __name__ == "__main__":
    main()

# 4
# 1
# 50
# 2
# 60
# 3
# 40
# 5
# 20


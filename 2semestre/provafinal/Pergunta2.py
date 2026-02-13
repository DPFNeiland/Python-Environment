from random import randint

# Considere uma classe chamada Leitura que representa as leituras de sensores de IoT.  
# A classe tem os seguintes atributos:
# id: int
# tipo: str --> ex.: "temperatura", "umidade", "pressão"
# valor: int
# unidade: float --> ex.: "C", "%", "kPa"

class Leitura:
    def __init__(self, id: int, tipo: str, valor: float, unidade: str):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.unidade = unidade


def CadastrarLeituras() -> list:
    Leituras = list()

    n = int(input("Digite a quantidade de Leituras: "))

    for _ in range(n):
        print("-" * 50)
        LeituraId = int(input("Digite o id (inteiro): "))
        LeituraTipo = str(input("Digite o tipo da leitura: "))
        LeituraValor = float(input("Digte o valor da leitura: "))
        LeituraUnidade = str(input("Digite a unidade de leitura: "))

        Leituras.append(
            Leitura(
                LeituraId,
                LeituraTipo,
                LeituraValor,
                LeituraUnidade
            )
        )
    return Leituras


def ImprimirLeituras(Leituras: list[Leitura]) -> list:
    quicksort(Leituras)

    print(f"ID     | Tipo           | Valor     | Unidade      ")
    print("-" * 50)
    for leitura in Leituras:
        print(f"{leitura.id:<7}",end="| ")
        print(f"{leitura.tipo:<15}",end="| ")
        print(f"{leitura.valor:<10}", end="| ")
        print(f"{leitura.unidade}")


# a) função que receba como parâmetro uma lista do tipo Leitura e também o id de uma leitura. A sua função deverá retornar True se o 
# id estiver na lista ou False caso contrário. Você deverá implementar a busca binária (não pode ser função pronta da linguagem). 
# Para utilizar a busca binária a lista deve estar ordenada (você pode utilizar qualquer método de ordenação, mas não pode utilizar
# funções prontas da linguagem).
def Procurar_Leitura(Leituras: list[Leitura], valor) -> bool:
    ini, fim = 0, len(Leituras) - 1

    while ini <= fim:
        meio = (ini + fim) // 2
        if Leituras[meio].id == valor:
            return True
        elif Leituras[meio].id < valor:
            ini = meio + 1
        else:
            fim = meio - 1
    return False


def quicksort(Leituras: list[Leitura], inicio = 0, fim = None):
    if fim is None:
        fim = len(Leituras) - 1
        
    if inicio < fim:
        pivo = particionar(Leituras, inicio, fim)
        quicksort(Leituras, inicio, pivo - 1)
        quicksort(Leituras, pivo + 1, fim)


def particionar(Leituras: list[Leitura], inicio: int, fim: int) -> int:
    k = randint(inicio, fim)
    Leituras[k], Leituras[fim] = Leituras[fim], Leituras[k]
    
    pivo = Leituras[fim].id
    i = inicio - 1
    
    for j in range(inicio, fim):
        if Leituras[j].id <= pivo:
            i += 1
            Leituras[i], Leituras[j] = Leituras[j], Leituras[i]

    Leituras[i + 1], Leituras[fim] = Leituras[fim], Leituras[i + 1]
    return i + 1

# b) função que receba como parâmetro uma lista de leituras e também um valor mínimo e máximo de leitura. A função deverá retornar 
# uma lista contendo as leituras que estão dentro do intervalo (fechado) mínimo e máximo recebidos como parâmetro. Você deverá 
# implementar a busca sequencial (não pode ser usar funções prontas da linguagem).
def Procurar_Valores_Intervalo_Leitura(Leituras: list[Leitura],ValorMin: float, ValorMax: float) -> list[Leitura]:
    LeiturasIntervalo = []

    for leitura in Leituras:
        if leitura.valor >= ValorMin and leitura.valor <= ValorMax:
            LeiturasIntervalo.append(leitura)


    return LeiturasIntervalo

def main():
    Leituras = CadastrarLeituras()
    ImprimirLeituras(Leituras)

    id = int(input("Digite o ID da Leitura que quer achar: "))
    print(Procurar_Leitura(Leituras, id))

    ValorMin = float(input("Digite o valor mínimo para procurar nas leituras: "))
    ValorMax = float(input("Digite o valor máximo para procurar nas leituras: "))

    ImprimirLeituras(Procurar_Valores_Intervalo_Leitura(Leituras, ValorMin, ValorMax))

if __name__ == "__main__":
    main()

# * Exemplo de Entrada de Teste:
# 4
# 3
# Temperatura
# 50
# °F
# 1
# Temperatura
# 68.5
# °F
# 4
# Temperatura
# 49
# °F
# 2
# Temperatura
# 22
# °F
# 5
# 49
# 60

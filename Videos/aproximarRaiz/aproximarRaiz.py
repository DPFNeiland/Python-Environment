

def calcularRaizQuadrada(N: float) -> float:
    cont = 9

    resp = N//10000 + 1

    while cont != 0:
        resp = (resp*resp+N)/2/resp
        cont -= 1

    return resp


def main():

    N = float(input("Digite um numero: "))

    
    print(f"A raiz quadrada desse numero eh: {calcularRaizQuadrada(N):.2f}")

if __name__ == "__main__":
    main()
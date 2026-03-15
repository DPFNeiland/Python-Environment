class No:
    def __init__(self, dado):
        self.dado = dado
        self.ant: No = None
        self.pos: No = None

class ListaDP:
    def __init__(self):
        self.tamanho = 0
        self.inicio: No = None
        self.fim: No = None

    def append(self, dado):
        dado = No(dado)

        if self.tamanho == 0:
            self.inicio = dado
            
        else:
            dado.ant = self.fim
            self.fim.pos = dado

        self.fim = dado
        self.tamanho += 1

    def imprimir(self):
        aux = self.inicio

        while aux:
            print(aux.dado, end=" ")
            aux = aux.pos
        print()

def rotacionar(lista: ListaDP, k: int):
    
    k = k % lista.tamanho

    if lista.tamanho == 1 or k == lista.tamanho or  k == 0 or lista.tamanho == 0:
        return
    
    # achar o novo da lista
    novo_inicio = lista.inicio
    for _ in range(k):
        novo_inicio = novo_inicio.pos

    novo_fim = novo_inicio.ant

    lista.fim.pos = lista.inicio
    lista.inicio.ant = lista.fim

    novo_inicio.ant = None
    novo_fim.pos = None

    lista.inicio = novo_inicio
    lista.fim = novo_fim

def main():
    lista = ListaDP()

    for v in map(int, input("Digite os valores da lista: ").split()):
        lista.append(v)
    
    rotacionar(lista, 2)

    lista.imprimir()

if __name__ == "__main__":
    main()
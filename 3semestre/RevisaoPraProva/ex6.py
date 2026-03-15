class No:
    def __init__(self, dado):
        self.dado = dado
        self.ant: No = None
        self.pos: No = None

class ListaDP:
    def __init__(self):
        self.tamanho = 0
        self.inicio = None
        self.fim = None

    def append(self, valor):
        valor = No(valor)

        if self.tamanho == 0:
            self.inicio = valor

        else:
            self.fim.pos = valor
            valor.ant = self.fim
        self.fim = valor
        self.tamanho += 1

    def show(self):
        aux: No = self.inicio

        while aux:
            print(f"{aux.dado}", end=" ")
            aux = aux.pos
        print()

    def search(self, valor):
        aux: No = self.inicio

        while aux:
            if aux.dado == valor:
                return aux

            aux = aux.pos
        
        return None


    def swap(self, valor1, valor2):
        valor1: No = self.search(valor1)
        valor2: No = self.search(valor2)
        
        if valor1 == self.inicio and valor1 == self.fim:
            valor2.pos = valor1
            valor1.ant = valor2

            valor2.ant = None
            valor1.pos = None

            self.inicio = valor2
            self.fim = valor1

        elif valor1 == self.inicio: 
            valor1.pos = valor2.pos
            valor2.pos.ant = valor1

            valor2.pos = valor1
            valor1.ant = valor2

            valor2.ant = None
            self.inicio = valor2 

        elif valor2 == self.fim:
            valor1.ant = valor2
            valor2.ant = valor1.ant

            valor2.pos = valor1
            valor1.ant = valor2

            valor1.pos = None
            self.fim = valor1

        elif valor1 and valor2:
            valor1.ant.pos = valor2
            valor2.ant = valor1.ant

            valor2.pos.ant = valor1
            valor1.pos = valor2.pos

            valor1.ant = valor2
            valor2.pos = valor1

def ordernar(lista: ListaDP):

    atual = lista.inicio

    while atual:
        aux = atual.pos

        while aux:
            if atual.dado > aux.dado:
                lista.swap(atual.dado, aux.dado)

            aux = aux.ant


        lista.show()

def main():
    transacoes = ListaDP()

    for v in map(int, input().split()):
        transacoes.append(v)

    transacoes.show()

    ordernar(transacoes)

    

if __name__ == "__main__":
    main()
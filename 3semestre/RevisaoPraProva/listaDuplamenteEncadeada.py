class No:

    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.posterior = None

class ListaDE:

    def __init__(self):
        self.tamanho = 0
        self.inicio: No = None
        self.fim: No = None

    
    def inserir_inicio(self, valor):

        dado = No(valor)

        if self.tamanho == 0:
            self.fim = dado

        else:
            dado.posterior = self.inicio
            self.inicio.anterior = dado

        self.inicio = dado
        self.tamanho += 1

    def inserir_final(self, valor):
        dado = No(valor)

        if self.tamanho == 0:
            self.inicio = dado

        else:
            dado.anterior = self.fim
            self.fim.posterior = dado

        self.fim = dado
        self.tamanho += 1


    def imprimir(self):

        aux = self.inicio

        while aux is not None:
            print(f"{aux.valor}", end=" ")
            aux = aux.posterior
        print()

    def procurar(self, valor):
        aux = self.inicio

        while aux is not None:
            if aux.valor == valor:
                return aux 
            aux = aux.posterior

        return None

    def remover_valor(self, valor):
        aux = self.procurar(valor)

        if aux is not None:
            if self.tamanho == 1:
                self.inicio = None
                self.fim = None
                self.tamanho -= 1

            elif aux == self.inicio:
                aux.posterior.anterior = None
                self.inicio = aux.posterior
                aux.posterior = None
                self.tamanho -= 1

            elif aux == self.fim:
                aux.anterior.posterior = None
                self.fim = aux.anterior
                aux.anterior = None
                self.tamanho -= 1

            else:
                aux.posterior.anterior = aux.anterior
                aux.anterior.posterior = aux.posterior
                aux.posterior = None
                aux.anterior = None
                self.tamanho -= 1
            

def main():
    lista = ListaDE()

    lista.inserir_inicio(10)
    lista.inserir_inicio(20)
    lista.inserir_inicio(30)
    lista.inserir_final(40)
    lista.inserir_final(50)

    lista.imprimir()

    print(lista.procurar(40))
    print(lista.procurar(70))

    lista.remover_valor(30)
    lista.remover_valor(50)
    lista.remover_valor(10)
    lista.imprimir()


if __name__ == "__main__":
    main()
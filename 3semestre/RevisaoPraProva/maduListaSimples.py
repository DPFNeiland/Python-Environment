class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.tamanho: int = 0
        self.inicio: No = None
        self.fim: No = None

    def inserir_final(self, dado):
        novo_dado = No(dado)

        if self.fim is None:
            self.tamanho += 1
            self.inicio = novo_dado
            self.fim = novo_dado

        else:
            self.tamanho += 1
            self.fim.proximo = novo_dado
            self.fim = novo_dado

    def imprimir(self):
        aux = self.inicio

        while aux is not None:
            print(aux.dado, end=" ")
            aux = aux.proximo
        print()

    
    def inserir_inicio(self, dado):
        novo_dado = No(dado)

        if self.inicio is None:
            self.tamanho += 1
            self.inicio = novo_dado
            self.fim = novo_dado
            
        else:
            self.tamanho += 1
            novo_dado.proximo = self.inicio
            self.inicio = novo_dado


def main():
    lista = ListaEncadeada()

    lista.inserir_final(10)
    lista.inserir_final(20)
    lista.inserir_final(30)
    lista.inserir_inicio(40)
    lista.inserir_inicio(50)

    lista.imprimir()

if __name__ == "__main__":
    main()
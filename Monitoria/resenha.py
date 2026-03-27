class No:
    def __init__(self, dado: any):
        self.dado: any = dado
        self.dir: No = None
        self.esq: No = None

class Lista_Duplamente_Encadeada:
    def __init__(self):
        self.tamanho: int = 0
        self.inicio: No = None
        self.fim: No = None

    def inserir_final(self, valor):
        valor = No(valor)

        if self.tamanho == 0:
            self.inicio = valor
        
        else: 
            valor.esq = self.fim
            self.fim.dir = valor

        self.fim = valor
        self.tamanho += 1

    def inserir_inicio(self, valor):
        valor = No(valor)

        if self.tamanho == 0:
            self.fim = valor

        else:
            valor.dir = self.inicio
            self.inicio.esq = valor

        self.inicio = valor
        self.tamanho += 1

    def imprimir(self):
        aux = self.inicio

        while aux is not None:
            print(f"{aux.dado}", end=" ")
            aux = aux.dir

lista = Lista_Duplamente_Encadeada()
lista.inserir_final(10)
lista.inserir_final(20)
lista.inserir_final(30)
lista.imprimir()
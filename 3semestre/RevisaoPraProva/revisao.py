class No:
    def __init__(self, dado: any):
        self.dado = dado
        self.direita: No = None
        self.esquerda: No = None

class Lista_Duplamente_Encadeada:
    def __init__(self):
        self.tamanho: int = 0
        self.inicio: No = None
        self.fim: No = None

    def inserir_final(self, valor: any):
        if self.tamanho == 0:
            aux = No(valor)
            self.tamanho += 1
            self.inicio = aux
            self.fim = aux

        else:
            aux = No(valor)
            self.tamanho += 1
            self.fim.direita = aux
            aux.esquerda = self.fim
            self.fim = aux

    def inserir_inicio(self, valor):

        if self.tamanho == 0:
            aux = No(aux)
            self.inicio = aux
            self.fim = aux
            self.tamanho += 1

        else:
            aux = No(valor)
            self.tamanho += 1
            aux.direita = self.inicio
            self.inicio.esquerda = aux
            self.inicio = aux

    def imprimir(self):
        aux = self.inicio

        while aux is not None:
            print(aux.dado)
            aux = aux.direita


lista = Lista_Duplamente_Encadeada()

lista.inserir_final(2)
lista.inserir_final(3)
lista.inserir_final(5)
lista.inserir_inicio(1)
lista.inserir_inicio(2)

lista.imprimir()

class No: 
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir_inicio(self, valor):
        novo = No(valor)

        # verifica se a lista está vazia
        if self.tamanho == 0:
            self.fim = novo
        
        else:
            novo.dir = self.inicio
            self.inicio.esq = novo


        self.inicio = novo
        self.tamanho += 1

    def inserir_final(self, valor):
        novo = No(valor)

        if self.tamanho == 0:
            self.inicio = novo


        else:
            novo.esq = self.fim
            self.fim.dir = novo
        
        self.fim = novo
        self.tamanho += 1


    def imprimir(self):
        aux = self.inicio
        while aux: # aux != None
            print(aux.dado, end=" ")
            aux = aux.dir

    def pesquisar(self, valor):
        aux = self.inicio
        
        while aux:
            if aux.dado == valor:
                return aux
            aux = aux.dir
        return None
    
    def remover(self, dado):
        aux = self.pesquisar(dado)

        if aux is not None:
            if self.tamanho == 1: # a lista tem apensa um valor
                self.inicio = None
                self.fim = None
                aux = None

            elif aux == self.inicio: # remove o 1° elemento
                aux.dir.esq = None
                self.inicio = aux.dir
                aux.dir = None
                aux = None

            elif aux == self.fim: # remove o último elemento
                aux.esq.dir = None
                self.fim = aux.esq
                aux.esq = None
                aux = None

            else: # o do meio
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
                aux.esq = None
                aux.dor = None
                aux = None
# programa principal

lista = Lista()
lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_inicio(30)
lista.inserir_final(30)
lista.inserir_final(40)

print()
lista.remover(30)
lista.remover(50)
lista.remover(10)

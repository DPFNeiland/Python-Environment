
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
        while aux:
            print(aux.dado, end=" ")
            aux = aux.dir

    def pesquisar(self, valor):
        aux = self.inicio

        while aux:
            if aux.dado ==valor:
                return aux
            aux = aux.dor
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


def main1():

    lista1 = list(map(int, input("Digite a primeira lista: ").split()))
    lista2 = list(map(int, input("Digite a segunda lista:").split()))

    listaDP = Lista()

    n = min(len(lista1), len(lista2))

    for i in range(n):
        listaDP.inserir_final(lista1[i])
        listaDP.inserir_final(lista2[i])

    if len(lista1) > len(lista2):
        for i in range(n, len(lista1)):
            listaDP.inserir_final(lista1[i])

    else:
        for i in range(n, len(lista2)):
            listaDP.inserir_final(lista2[i])

    listaDP.imprimir()

def intercalar(l1: Lista, l2: Lista) -> Lista:
    nova = Lista()

    p1 = l1.inicio    
    p2 = l2.inicio

    while p1 is not None and p2 is not None:
        nova.inserir_final(p1.dado)
        nova.inserir_final(p2.dado)

        p1 = p1.dir
        p2 = p2.dir


    while p1 is not None:
        nova.inserir_final(p1.dado)
        p1 = p1.dir


    while p2 is not None:
        nova.inserir_final(p2.dado)
        p2 = p2.dir



    return nova



def main2():
    premium = Lista()
    comum = Lista()

    premium.inserir_final(10)
    premium.inserir_final(10)
    premium.inserir_final(10)
    premium.inserir_final(20)
    premium.inserir_final(30)

    comum.inserir_final(1)
    comum.inserir_final(2)
    comum.inserir_final(3)

    lista = intercalar(premium, comum)
    lista.imprimir()

if __name__ == "__main__":
    main2()
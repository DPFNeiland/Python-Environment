
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
                aux.dir = None
                aux = None


def rotacionar(lista: Lista, n):
    
    # calcula o valor do deslocamento quando n for  maior que o tamanho    

    # não há rotação
    n = n % lista.tamanho
    if n == 0 or lista.tamanho == 1:
        return lista

    # auxiliar para percorrer a lista e encontrar o "novo" início    
    aux = lista.inicio
    for _ in range(n):
        aux = aux.dir

    # configura o novo inicia e o novo fim
    novo_inicio = aux
    novo_fim = aux.esq

    novo_inicio.esq = None
    novo_fim.dir = None

    lista.fim.dir = lista.inicio
    lista.inicio.esq = lista.fim

    lista.fim = novo_fim
    lista.inicio = novo_inicio

    return lista

def main1():
    lista = Lista()

    lista.inserir_final(10)
    lista.inserir_final(20)
    lista.inserir_final(30)
    lista.inserir_final(40)
    lista.inserir_final(50)
    lista.inserir_final(60)


    for n in range(100):
        rotacionar(lista, n)

        lista.imprimir()
        print()


if __name__ == "__main__":
    main1()
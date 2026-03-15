
class No:
    def __init__(self, valor):
        self.valor = valor
        self.pos = None
        self.ant = None



class Lista:

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
        aux: No = self.inicio

        while aux:
            print(aux.valor, end=" ")
            aux = aux.pos


def intercalar(ListaA: Lista, ListaB: Lista) -> Lista:
    '''
        ### Intercalar
        retornar a intercalação dessas listas
    '''
    aux1 = ListaA.inicio
    aux2 = ListaB.inicio
    nova_lista = Lista()

    while aux1 and aux2:
        nova_lista.append(aux1.valor)
        nova_lista.append(aux2.valor)

        aux1 = aux1.pos
        aux2 = aux2.pos

    while aux1:
        nova_lista.append(aux1.valor)
        aux1 = aux1.pos

    while aux2:
        nova_lista.append(aux2.valor)
        aux2 = aux2.pos

    return nova_lista


def main():
    listaPremium = Lista()
    listaComum = Lista()

    for v in map(int, input("Digite a lista de Clientes Premium: ").split()):
        listaPremium.append(v)

    for v in map(int, input("Digite a lista de Clientes Comuns: ").split()):
        listaComum.append(v)
    

    nova_lista = intercalar(listaPremium, listaComum)

    nova_lista.imprimir()
if __name__ == "__main__":
    main()
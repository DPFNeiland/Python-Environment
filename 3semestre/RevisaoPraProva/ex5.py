class No:
    def __init__(self, dado):
        self.dado = dado
        self.ant: No = None
        self.pos: No = None


class ListaDP:
    def __init__(self):
        self.tamanho: int = 0
        self.inicio: No = None
        self.fim: No = None 

    def append(self, valor):
        valor =  No(valor)

        if self.tamanho == 0:
            self.inicio = valor

        else:
            valor.ant = self.fim
            self.fim.pos = valor

        self.fim = valor
        self.tamanho += 1

    def print(self):
        aux = self.inicio

        while aux:
            print(f"{aux.dado}", end=" ")
            aux = aux.pos

        print()

    def search(self, valor):

        if valor:
            aux = self.inicio

            while aux:
                if aux.dado == valor:
                    return aux

                aux = aux.pos

        return None

    def remove(self, valor):
        aux = self.search(valor)

        if aux:
            if self.tamanho == 1:
                self.inicio = None
                self.fim = None
                valor = None
                

            elif self.inicio.dado == valor:
                self.inicio = self.inicio.pos
                self.inicio.ant.pos = None
                self.inicio.ant = None

            elif self.fim.dado == valor:
                self.fim = self.fim.ant
                self.fim.pos.ant = None
                self.fim.pos = None
            
            else:
                aux.ant.pos = aux.pos
                aux.pos.ant = aux.ant
                aux = None
            
            self.tamanho -= 1

def remover_repitidos(lista: ListaDP):
    atual = lista.inicio

    while atual:

        aux = atual.pos

        while aux:
            if aux.dado == atual.dado:
                lista.remove(aux.dado)
                atual = aux

            aux = aux.pos

        atual = atual.pos


 
def main():
    sensor = ListaDP()
    for v in map(int, input().split()):
        sensor.append(v)


    print("Lista Original: ", end="")
    sensor.print()

    remover_repitidos(sensor)

    print("Após remover repetições consecutivas: ", end="")
    sensor.print()




if __name__ == "__main__":
    main()
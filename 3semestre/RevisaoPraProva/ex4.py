class No:
    def __init__(self, dado):
        self.dado = dado
        self.ant: No = None
        self.pos: No = None


class ListaDP:
    def __init__(self):
        self.tamanho: int = 0
        self.inicio: No = None
        self.pos: No = None

    def append(self, valor):
        valor = No(valor)

        if self.tamanho == 0:
            self.inicio = valor

        else:
            self.fim.pos = valor
            valor.ant = self.fim

        self.tamanho += 1
        self.fim = valor
    
    def aquiles(self, valor = None):

        if not valor:
            self.fim.pos = self.inicio
            self.inicio.ant = self.fim
            self.fim = None


        else:
            aux = self.search(valor)

            if aux:
                self.fim.pos = aux
                self.fim = None

    
        
    def search(self, valor):

        aux = self.inicio

        while aux:

            if aux.dado == valor:
                return aux
            aux = aux.pos
        
        return None

    def print(self):
        aux = self.inicio

        while aux:
            print( f"{aux.dado} ", end=" ")
            aux = aux.pos
        print()    

def tem_ciclo(lista: ListaDP):
    ciclo = False

    if lista.tamanho == 0 or lista.tamanho == 1:
        ciclo = False

    else:
        coelho: No = lista.inicio.pos.pos
        tartaruga: No = lista.inicio.pos

        while coelho:
            if coelho == lista.fim:
                break
            
            elif coelho == tartaruga:
                ciclo = True
                break

            coelho = coelho.pos.pos
            tartaruga = tartaruga.pos



    return ciclo





def main():
    listaSemCiclo = ListaDP()

    listaSemCiclo.append(10)
    listaSemCiclo.append(20)
    listaSemCiclo.append(30)
    listaSemCiclo.append(40)
    listaSemCiclo.append(50)
    listaSemCiclo.append(60)
    listaSemCiclo.append(70)

    listaSemCiclo.print()

    print(listaSemCiclo.search(20))
    print(listaSemCiclo.search(-1))


    print(f"Tem ciclo: {tem_ciclo(listaSemCiclo)}")

    listaSemCiclo.aquiles(-1)
    listaSemCiclo.aquiles(30)

    print(f"Tem ciclo: {tem_ciclo(listaSemCiclo)}")




if __name__ == "__main__":
    main()
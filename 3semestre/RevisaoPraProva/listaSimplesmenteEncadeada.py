class No:

    def __init__(self, dado, prox = None):
        self.dado = dado
        self.prox: No = prox

class Lista:

    def __init__(self):
        self.inicio: No = None
        self.fim: No = None

    def inserir_fim(self, dado):
        valor = No(dado, None)
        if self.fim is not None:
            self.fim.prox = valor
        
        else:
            self.inicio = valor

        self.fim = valor

    def inserir_inicio(self, dado):
        valor = No(dado, None)
        if self.inicio is not None:
            valor.prox = self.inicio

        else:
            self.fim = valor
        self.inicio = valor
        

    def imprimir(self):
        aux = self.inicio
        while aux is not None:
            print(f"{aux.dado}", end=" ")

            aux = aux.prox
        print()

    def procurar(self, valor):
        aux = self.inicio
        while aux is not None:

            if aux.dado == valor:
                return aux
            
            aux = aux.prox
        return None
    
    def remover(self, valor): 

        achou = self.procurar(valor)

        if achou is not None:
            if achou == self.inicio:
                self.inicio = achou.prox
            
            else:
                anterior = self.inicio
                while anterior.prox is not achou:
                    anterior = anterior.prox
                
                if achou == self.fim:
                    anterior.prox = None
                    self.fim = anterior
                
                else:
                    anterior.prox = achou.prox
            aux = None
        
def main():
    lista = Lista()

    w = 10
    x = 20
    y = 30
    z = 40

    lista.inserir_fim(w)
    lista.remover(w)
    lista.inserir_fim(w)

    lista.imprimir()

if __name__ == "__main__":
    main()

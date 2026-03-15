
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

class Carro:
    def __init__(self, marca: str, modelo: str, valor: float):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor

    def __str__(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo}\nValor: R$ {self.valor}\n\n"

def main():
    lista = Lista() 
    lista.inserir_final(Carro("BMW", "x7", 750000.0))
    lista.inserir_final(Carro("audi", "q5", 35000))

    lista.imprimir()





if __name__ == "__main__":
    main()

class Carro:
    def __init__(self, marca: str, modelo: str, valor: float):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor

    def __str__(self):
        return f"Marca: {self.marca}\tModelo: {self.modelo}\tValor: R$ {self.valor}\n\n"

class No:
    def __init__(self, dado):
        self.dado: any = dado
        self.ant: No = None
        self.pos: No = None

class Lista:
    def __init__(self):
        self.tamanho: int = 0
        self.inicio: No = None
        self.fim: No = None

    def append(self, dado):
        valor = No(dado)

        if self.tamanho == 0:
            self.inicio = valor

        else:
            self.fim.pos = valor
            valor.ant = self.fim

        self.fim = valor
        self.tamanho += 1

    def search_model(self, modelo: str):
        aux = self.inicio

        while aux:
            if aux.dado.marca == modelo:
                return aux.dado
            aux = aux.pos

        return "Carro não encontrado"
    
    def search_expensive(self):

        if self.tamanho == 0:
            return "Nenhum carro no sistema."
        
        else:
            maxi = Carro("", "", -1)
            carro = self.inicio
            
            while carro:

                if carro.dado.valor > maxi.valor:
                    maxi = carro.dado

                carro = carro.pos

            return maxi
        
    def calculate_mean(self):

        if self.tamanho == 0:
            return "Nenhum carro no sistema"

        else:
            media = 0
            carro = self.inicio

            while carro:
                media += carro.dado.valor
                carro = carro.pos

            return "Média de preço dos carros: R$" + str(int(media/self.tamanho*100)/100)


    def __str__(self):

        if self.tamanho == 0:
            return "Não existe nenhum carro no sistema: "
        
        else:
            aux = self.inicio
            resp = ""
            while aux:
                resp += f"{aux.dado}"
                aux = aux.pos
            
            return resp
            

def main():
    Concessionaria = Lista()
    n = 2
    funcs = ["1- Cadastrar carro", 
            "2- Listar carros", 
            "3- Buscar carros pelo modelo", 
            "4- Encontrar o carro mais caro",
            "5- Calcular o valor médio dos carros",
            "6- Sair do sistema"]

    while True:
        for func in funcs:
            print(func)

        n = int(input())

        match n:
            case 1:
                marca = input("Digite a marca do carro: ")
                modelo = input("Digite o modelo do carro: ")
                valor = float(input("Digite o valor do carro: "))

                Concessionaria.append(Carro(marca, modelo, valor))
            
            case 2:
                print(Concessionaria)
            
            case 3:
                modelo = input("Digite o modelo do carro: ")
                resultado = Concessionaria.search_model(modelo)

                print(resultado)

            case 4:
                resultado = Concessionaria.search_expensive()

                print(resultado)

            case 5:
                resultado = Concessionaria.calculate_mean()

                print(resultado)

            case 6:
                break
                
            case _:
                print("Valor inválido!!!!")

        print("\n\n\n")





if __name__ == "__main__":
    main()
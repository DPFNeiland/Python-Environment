

class Item:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
# class para definir os dados e as funcionalidades do carrinho
class Carrinho:
    def __init__(self):
       self.itens: list[dict[str, Item]] = []
        
    # método para adicionar um item no carrinho
    def adicionar_item(self, nome: str, preco: float, quantidade: int):
        self.itens.append({nome: Item(nome, preco, quantidade)})
        
    # método para calcular e retornar o valor total da compra
    def total(self):
        soma = 0
        for i in self.itens:
            item = i.values()
            soma = soma + item.preco * item.quantidade
        return soma
    
    
# programa principal 
carrinho = Carrinho()
carrinho.adicionar_item("Lápix 2 cores", 5.99, 2)

print(carrinho.total())
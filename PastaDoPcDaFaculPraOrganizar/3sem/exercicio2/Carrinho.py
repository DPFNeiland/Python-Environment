
class Item:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Carrinho:
    def __init__(self):
        self.lista = []
        
    def adicionar_item(self, item: Item):
        
        n = len(self.lista)
        for i in range(n):
            if self.lista[i].nome == item.nome:
               self.lista[i].quantidade += item.quantidade
               return True
            
        self.lista.append(item)
        return False 
    
    def remover_item(self, nome: str):
        n = len(self.lista)
        for i in range(n):
            if self.lista[i].nome == nome:
               self.lista.remove(self.lista[i])
               return True            
        return False 
    
    def atualizar_quantidade(self, nome, quantidade):
        n = len(self.lista)
        for i in range(n):
            if self.lista[i].nome == nome:
               self.lista[i].quantidade = quantidade
               if quantidade <= 0:
                   self.remover_item(nome)
                   
               return True            
        return False 
    
    def listar_itens(self):
        
        n = len(self.lista)
        print("Listagem de itens no carrinho")
        for i in range(n):
            print(f"Nome: {self.lista[i].nome}\nPreco: {self.lista[i].preco}\nQtd: {self.lista[i].quantidade}\n\n")
    
    
produto1 = Item("Teclado reddragon Red", 399.90, 1)
produto2 = Item("Memória RAM 16gb ddr4", 1599.99, 1)
produto3 = Item("Memória RAM 16gb ddr4", 1599.99, 1)
produto4 = Item("SSD sodimm 2 tera", 2000.99, 2)
    
Meu_Carrinho = Carrinho()

print("TESTE 1-------------------------------------")
print(Meu_Carrinho.adicionar_item(produto1))
print(Meu_Carrinho.adicionar_item(produto2))
print(Meu_Carrinho.adicionar_item(produto3))
print(Meu_Carrinho.adicionar_item(produto4))

Meu_Carrinho.listar_itens()

print("TESTE 2-------------------------------------")
Meu_Carrinho.remover_item("Memória RAM 16gb ddr4")

Meu_Carrinho.listar_itens()


print("TESTE 3-------------------------------------")
print(Meu_Carrinho.adicionar_item(produto2))
    
    
Meu_Carrinho.atualizar_quantidade("SSD sodimm 2 tera", 1)
Meu_Carrinho.atualizar_quantidade("Teclado reddragon Red", 0)

Meu_Carrinho.listar_itens()


print("TESTE 4-------------------------------------")
print(Meu_Carrinho.adicionar_item(produto1))
print(Meu_Carrinho.adicionar_item(produto4))

Meu_Carrinho.listar_itens()
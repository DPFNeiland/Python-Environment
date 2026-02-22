
class Produto:
    def __init__(self, codigo: str, preco: float) -> None:
        self.codigo = codigo
        self.preco = preco

def cadastra(d: dict[str, Produto], p: Produto) -> None:
    d[p] = p

produtos: dict[str, Produto] = {}
p = Produto("X1", 9.99)
cadastra(produtos, p)
print(len(produtos))
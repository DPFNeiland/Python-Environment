

estoque = {
    "produto1": (100, 50),
    "produto2": (200, 30),
    "produto3": (150, 20),
    "produto4": (300, 10)
}

def calcular_valor_total(estoque):
    valor_total = 0
    for produto, (preco, quantidade) in estoque.items():
        valor_total += preco * quantidade
    return valor_total

print(calcular_valor_total(estoque))
precos = {  
    "arroz": 22.5, 
    "feijao": 9.8, 
    "leite": 4.7, 
    "pao": 1.5 
}
 
vendas = [ 
    ["arroz", "feijao", "feijao", "leite"], 
    ["pao", "pao", "pao", "leite"], 
    ["arroz", "leite"], 
    ["feijao", "feijao", "feijao"] 
]

# a) Calcule o total de cada venda e armazene os resultados em uma lista chamada c.
def Calcular_Total_Cada_Venda(vendas: list[list], precos: dict) -> list:
    totais_venda = []
    
    for vendas_do_dia in vendas:
        soma = 0
        
        for produto in vendas_do_dia:
            soma += precos.get(produto)    
    
        totais_venda.append(soma)

    
    return totais_venda

# b) Calcule o faturamento total (soma de todas as vendas).
def Calcular_Faturamento_Total(totais_vendas: list) -> float:
    soma = 0
    for valor in totais_vendas:
        soma += valor
    
    return soma

# c) Gere um dicionário qtd_por_item com a quantidade total vendida de cada produto.
def Calcular_Quantidade_Total_Vendida(vendas: list[list]) -> dict:
    qtd_por_item = {}
    
    items = []
    
    for venda_do_dia in vendas:
        for venda in venda_do_dia:
            if venda in items:
                qtd_por_item[venda] += 1
            else:
                qtd_por_item[venda] = 1
                items.append(venda)
    
    return qtd_por_item
    
# d) Identifique: 
# - o produto mais vendido (maior quantidade); 
# - o produto com maior faturamento individual (quantidade × preço).
def Calcular_Produto_mais_vendido(qtd_por_item: dict) -> list:

    maior = -1
    nome = []
    
    for produto, qtd in qtd_por_item.items():
        if qtd > maior:
            nome = []
            maior = qtd
        
        if qtd == maior:
            nome.append(produto)
            
    return nome

def Calcular_Produto_Maior_Faturamento(qtd_por_item: dict, precos: dict):

    maior_faturamento = -1
    nome = []
    
    for produto, qtd in qtd_por_item.items():
        preco = precos.get(produto)
        faturamento = qtd*preco
        if faturamento > maior_faturamento:
            nome = []
            maior_faturamento = faturamento
        
        if faturamento == maior_faturamento:
            nome.append(produto)


    return nome

# e) Calcule o ticket médio da loja (faturamento total ÷ número de vendas). 
def Calcular_Ticker_Medio(faturamento: float, vendas: list[list]) -> float:
    
    return faturamento/len(vendas)

# f) Organize as informações em um dicionário relatorio com o formato: 
# relatorio = { 
#   "totais_venda": [...], 
#   "faturamento_total": ..., 
#   "qtd_por_item": {...}, 
#   "mais_vendido": "...", 
#   "mais_faturado": "...", 
#   "ticket_medio": ... 
# } 

def gerar_relatorio(vendas: list[list], precos: dict) -> dict:
    totais_vendas = Calcular_Total_Cada_Venda(vendas, precos)
    qtd_por_item= Calcular_Quantidade_Total_Vendida(vendas)
    faturamento = Calcular_Faturamento_Total(totais_vendas)
    
    return {
        "totais_venda": totais_vendas,
        "faturamento_total": faturamento,
        "qtd_por_item": Calcular_Quantidade_Total_Vendida(vendas),
        "mais_vendido": Calcular_Produto_mais_vendido(qtd_por_item),
        "mais_faturado": Calcular_Produto_Maior_Faturamento(qtd_por_item, precos),
        "ticket_medio": Calcular_Ticker_Medio(faturamento, vendas)
    }

def main():
    
    relatorio = gerar_relatorio(vendas, precos)    
    
    print(relatorio)

if __name__ == "__main__":
    main()
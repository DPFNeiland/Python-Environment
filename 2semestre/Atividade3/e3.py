pedidos = { 
    "P001": {"cliente": "Ana", "produtos": {"Mouse": 80.0, "Teclado": 120.0}}, 
    "P002": {"cliente": "Bruno", "produtos": {"Monitor": 700.0}}, 
    "P003": {"cliente": "Ana", "produtos": {"Cabo HDMI": 40.0, "Mouse": 80.0}}, 
    "P004": {"cliente": "Carla", "produtos": {"Cadeira Gamer": 950.0}} 
}

# a) Calcular o total gasto em cada pedido. Exemplo: {"P001": 200.0, "P002": 700.0, ...}. 
def Calcular_Total_Gasto_Pedido(pedidos: dict) -> dict:
    
    Total_Gasto_Pedido = {}
    soma = 0
    for pedido, informacoes in pedidos.items():
        soma = 0
        for precos in informacoes.get("produtos").items(): 
            soma += precos[1]
            
        Total_Gasto_Pedido[pedido] = soma
            
    return Total_Gasto_Pedido

# b) Calcular o total gasto por cliente. Exemplo: {"Ana": 320.0, "Bruno": 700.0, "Carla": 950.0}. 
def Calcular_Total_Gasto_Cliente(pedido: dict) -> dict:
    nome_Lista_Cliente = []
        
    Total_Gasto_Cliente = {}
    soma = 0
 
    for informacoes in pedidos.values():
        nome_cliente = informacoes.get("cliente")
        
        soma = 0
        for produtos in informacoes.get("produtos").values(): 
            soma += produtos
        
        if nome_cliente in nome_Lista_Cliente:
            Total_Gasto_Cliente[nome_cliente] += soma
        else:
            Total_Gasto_Cliente[nome_cliente] = soma
            nome_Lista_Cliente.append(nome_cliente)
            
    return Total_Gasto_Cliente

# c) Identificar o cliente que mais gastou. 
def identificar_Cliente_Mais_Gastou(clientes: dict) -> list:
    
    maior = -1
    nome = []
    
    for cliente, gasto in clientes.items():
        if gasto > maior:
            maior = gasto
            nome = []
        
        if gasto == maior:
            nome.append(cliente)
            
    return nome
        

# d) Calcular e imprimir o faturamento total da loja.
def Calcular_Faturamento_Loja(clientes) -> float:
    total = 0
    for gasto in clientes.values():
        total += gasto

    return total

def main():
    print(Calcular_Total_Gasto_Pedido(pedidos))
    
    clientes = Calcular_Total_Gasto_Cliente(pedidos)
    print(clientes)
    
    print(identificar_Cliente_Mais_Gastou(clientes))
    
    print(Calcular_Faturamento_Loja(clientes))
if __name__ == "__main__":
    main()

# Função que vai calcular

def Calcular_Graos(n: int) -> int:    
    
    # m, h, g = 10
    # g é um argumento opcional
    '''
    Calcula a quantidade de grãos o monge precisa
    
    Variáveis: Quantidade de casas do tabuleiro
    
    Argumento opcional: Nenhum
    '''
    
    return 2**n - 1



# Programa principal

N = 64

print(f"A quantidade de grãos é: {Calcular_Graos(N)}")
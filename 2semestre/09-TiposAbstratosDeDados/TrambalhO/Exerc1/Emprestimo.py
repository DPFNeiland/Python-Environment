import math

class Emprestimo:

    # Codifique uma classe chamada Emprestimo que contenha os seguintes atributos: 
    # valor financiado (float), taxa de juros mensal (float), número de parcelas (int), 
    # identificador do empréstimo (str) e nome do cliente (str).
    def __init__(
        self, 
        valor_financiado: float = 1.0,  
        taxa_de_juros_mensal: float = 0.01,
        numero_de_parcelas: float = 1,
        identificador_do_empréstimo: str = "Não Identificado", 
        nome_do_cliente: str = "Não identificado"
        ):

        self.valor_financiado = valor_financiado
        self.taxa_de_juros_mensal = taxa_de_juros_mensal
        self.numero_de_parcelas = numero_de_parcelas
        self.identificador_do_empréstimo = identificador_do_empréstimo
        self.nome_do_cliente = nome_do_cliente

    # a) Método para calcular e retornar o valor da parcela (fixa) pelo método PRICE. 
    def calcular_parcelar(self) -> float:
        if self.taxa_de_juros_mensal == 0:
            return self.valor_financiado/self.numero_de_parcelas
        return self.valor_financiado * self.taxa_de_juros_mensal / 100 / (1 - (pow(1 + self.taxa_de_juros_mensal/100,-self.numero_de_parcelas)))        
    
    # b) método para retornar o saldo devedor após o pagamento da k-ésima parcela (k ≥ 0). 
    def calcular_saldo_devedor(self, k: int) -> float | str:

        if k <= self.numero_de_parcelas:
            taxa = self.taxa_de_juros_mensal/100

            primeira_parte = self.valor_financiado*pow((1+taxa), k)
            segunda_parte = self.calcular_parcelar()*(pow(1 + taxa, k) - 1)/taxa
            
            return primeira_parte - segunda_parte
        return "Parcela inválida"
    
    # c) método para calcular e retornar o valor total de juros pagos ao final do 
    # financiamento.
    def calcular_juros_pago(self) -> float:
        return self.numero_de_parcelas*self.calcular_parcelar() - self.valor_financiado
    
from Emprestimo import Emprestimo
from typing import List
from random import randint

def validar_input_float(variavel, texto) -> float:

    variavel = 0
    
    while variavel <= 0:
        variavel = float(input(texto))

    return variavel


def cadastrar_emprestimo(n: int) -> List:

    Emprestimos = []
    valor_financiado = 0
    taxa_de_juros_mensal = 0
    numero_de_parcelas = 0
    
    print("-" * 50)
    for _ in range(n):

        valor_financiado = validar_input_float(
            valor_financiado, 
            "Digite o valor financiado R$: "
        )
        
        taxa_de_juros_mensal = validar_input_float(
            taxa_de_juros_mensal, 
            "Digite a taxa de juros mensal em %: "
        )

        numero_de_parcelas = validar_input_float(
            numero_de_parcelas,
            "Digite o número de parcelas: "
        )

        
        identificador_do_empréstimo = str(input("Digite o valor ID do empréstimo: "))
        nome_do_cliente = str(input("Digite o nome do cliente: "))

        Emprestimos.append(Emprestimo(
            valor_financiado,
            taxa_de_juros_mensal,
            numero_de_parcelas,
            identificador_do_empréstimo,
            nome_do_cliente
        ))
        print("-" * 50)

    return Emprestimos


def quicksort(lista: List[Emprestimo], inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
        
    if inicio < fim:
        pivo = particionar(lista, inicio, fim)
        quicksort(lista, inicio, pivo - 1)
        quicksort(lista, pivo + 1, fim)

def particionar(lista: List[Emprestimo], inicio: int, fim: int) -> int:
    k = randint(inicio, fim)
    lista[k], lista[fim] = lista[fim], lista[k]
    
    pivo = lista[fim].calcular_juros_pago()
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j].calcular_juros_pago() > pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1


# d) listagem contendo o identificador do empréstimo, o valor da parcela, 
# o valor dos juros totais  
def imprimir_emprestimo(Emprestimos: List[Emprestimo]) -> None:

    quicksort(Emprestimos)

    print("[Ranking por Juros Total]")
    print("ID   - QtdParcelas | Valor Financiado(R$) | Valor de Cada Parcela (R$) | Juros Total (R$) | Custo Total (R$)")

    i = 0
    for emprestimo in Emprestimos:
        
        parcela = emprestimo.calcular_parcelar()
        juros = emprestimo.calcular_juros_pago()
        
        i += 1
        print(f"{emprestimo.identificador_do_empréstimo:<5}", end="- ")
        print(f"{str(int(emprestimo.numero_de_parcelas)) + "x":<11}", end=" | ")
        print(f"{str(int(emprestimo.valor_financiado*100)/100):<20}", end=" | ")
        print(f"{str(int(parcela*100)/100):<26}", end=" | ")
        print(f"{str(int(juros*100)/100):<16}", end=" | ")
        print(f"{str(int((emprestimo.valor_financiado + juros)*100)/100)}")


# e) listagem contendo o identificador do plano e o saldo devedor após o pagamento de 12 
# parcelas.

def imprimir_saldo_apos_12_parcelas(Emprestimos: List[Emprestimo]) -> None:
    
    print("[Saldos após 12 parcelas]")
    print("ID   - QtdParcelas | Saldo após 12 parcelas (R$)")

    for emprestimo in Emprestimos:
        print(f"{emprestimo.identificador_do_empréstimo:<5}", end="- ")
        print(f"{str(int(emprestimo.numero_de_parcelas)) + "x":<11}", end=" | ")

        saldoDevedor = emprestimo.calcular_saldo_devedor(12) if emprestimo.numero_de_parcelas >= 12 else 0

        print(f"{int(saldoDevedor*100)/100}")
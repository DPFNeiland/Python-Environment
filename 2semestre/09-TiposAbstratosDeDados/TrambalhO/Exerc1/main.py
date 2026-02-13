import modules

def main():
    
    # Escreva um programa de teste que faça a leitura dos dados via terminal, gere 
    # objetos do tipo Emprestimo e armazene em uma lista. 

    n = -1
    listaEmprestimos = []

    while n <= 0:
        n = int(input("Digite a quantidade de empréstimo para cadastrar: "))

    listaEmprestimos = modules.cadastrar_emprestimo(n)

    modules.imprimir_emprestimo(listaEmprestimos)

    modules.imprimir_saldo_apos_12_parcelas(listaEmprestimos)

if __name__ == "__main__":
    main()
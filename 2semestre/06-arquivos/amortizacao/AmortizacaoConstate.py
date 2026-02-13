from random import randint 
I = randint(1,5)/100
N = 12
nomedoarquivo = "financiamentos.txt"
width = 10

with open(nomedoarquivo, "r", encoding="utf-8") as arquivo:
    print(f"Juros: {I}\tParcelas: {N}")
    
    for linha in arquivo:
        linha = linha.strip()
        
        if linha == "":
            continue
        
        nome, valor = linha.split(";")
        valor = float(valor)
        
        pmt = valor*I*(I+1)**N/((I + 1)**N-1)
        
        print(f"{nome:<{width}}\t Valor do finacimanento R$ {valor:.2f}\t valor da parcela: R$ {pmt:.2f}")
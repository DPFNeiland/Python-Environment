
linha = int(input("Total de linhas --> "))
coluna = int(input("Total de colunas --> "))

m = []

for i in range(linha):
    aux = []

    for j in range(coluna):
        aux.append(int(input("valor --> ")))
    m.append(aux)   
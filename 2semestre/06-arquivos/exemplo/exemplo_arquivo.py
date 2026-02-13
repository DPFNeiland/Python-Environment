
# bloco de leitura de arquivo

with open("aluno.txt", "r") as arquivo:
    aprovados = 0
    
    for linha in arquivo:
        linha = linha.strip()
        nome, nota1, nota2 = linha.split(";")
        media = (float(nota2) + float(nota1)) /2
        
        print(f"{nome} --> {media:.2f}")

        if media >= 7.0:
            aprovados += 1
    print(f"Quantidade de aprovados: {aprovados}")
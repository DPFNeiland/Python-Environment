
def main():
    acoes = [3, 1, 1, 8, 5, 3]
    soma = 0

    for i in range(len(acoes)):
        soma += acoes[i]
        print(f"Média Pré-fixada: {soma/(i + 1)}")
        
if __name__ == "__main__":
    main()
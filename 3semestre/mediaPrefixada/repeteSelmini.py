
# lista = [7, 3, 4, 2, 3, 5, 2]

def pesquisar(lista) -> int:
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return lista[i]
    return -1


def main():
    lista = [7,2,4,8,2,4]
    print(pesquisar(lista))
    
if __name__ == "__main__":
    main()
    
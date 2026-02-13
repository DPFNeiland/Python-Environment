from random import randint
import time

from random import randint

def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
        
    if inicio < fim:
        pivo = particionar(lista, inicio, fim)
        quicksort(lista, inicio, pivo - 1)
        quicksort(lista, pivo + 1, fim)

def particionar(lista, inicio, fim) -> int: 
    
    pivo = lista[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j] > pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

def FuncaoDoCaba(a: list[int]) -> None:
    n = len(a)
    if n < 2:
        return
    
    i = 1
    while i < n:
        x = a[i]
        if x>= a[i - 1]:
            i += 1
            continue

        inicio, fim =  0, i
        while inicio < fim:
            meio = (inicio + fim) // 2
            if a[meio] <= x:
                inicio = meio + 1
            else:
                fim = meio

        j = i
        while j > inicio:
            a[j] = a[j - 1]
            j -= 1
        a[inicio] = x
        i += 1


def medir_tempo(algoritmo, lista: list) -> float:
    lista_aux = lista.copy()
    inicio = time.perf_counter()
    algoritmo(lista_aux)
    fim = time.perf_counter()
    return (fim - inicio) * 1000

def gerar_lista(n: int) -> list:
    lista = []
    for _ in range(n):
        lista.append(randint(1, n ** 3))

    return lista

def main():
    print('Comparação entre os métodos de ordenação')
    print()

    tamanho = [100, 1000, 10000]
    
    for i in range(1, 11):
        print(f"Tamanho da lista {i} {"-" * 40}")

        lista = gerar_lista(i) 
        tempo_quickSort = medir_tempo(quicksort, lista)
        tempo_aluno = medir_tempo(FuncaoDoCaba, lista)

        print(f"Tempo quicksort {tempo_quickSort:.3f}")
        print(f"Tempo do aluno {tempo_aluno:.3f}",end="\n\n")

    print("-" * 40)
    print("-" * 40)
    print("-" * 40)

    for i in range(len(tamanho)):
        print(f"Tamanho da lista {tamanho[i]} {"-" * 40}")

        lista = gerar_lista(tamanho[i]) 
        tempo_quickSort = medir_tempo(quicksort, lista)
        tempo_aluno = medir_tempo(FuncaoDoCaba, lista)

        print(f"Tempo quicksort {tempo_quickSort:.3f}")
        print(f"Tempo do aluno {tempo_aluno:.3f}",end="\n\n")
        print("-" * 40)

        
if __name__ == "__main__":
    main()
    
    
    
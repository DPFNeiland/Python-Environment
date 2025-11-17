from random import randint
import util
import time

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
    tamanho = [100, 1000, 10000, 100000]
    print('Comparação entre os métodos de ordenação')
    print()
    
    for n in tamanho:
        print(f"Lista de tamanho {n}: ")
        lista = gerar_lista(n)
        # tempo_bolha = medir_tempo(util.BubbleSort, lista)
        # tempo_selecao = medir_tempo(util.SelectionSort, lista)
        # tempo_insercao = medir_tempo(util.InsertionSort, lista)
        tempo_quickSort = medir_tempo(util.quickSort, lista)
        # print(f"Tempo bolha {tempo_bolha:.3f}")
        # print(f"Tempo seleçãp {tempo_selecao:.3f}")
        # print(f"Tempo bolha {tempo_insercao:.3f}")
        print(f"Tempo quicksort {tempo_quickSort:.3f}")
        print("-" * 40)
        
if __name__ == "__main__":
    main()
    
    
    

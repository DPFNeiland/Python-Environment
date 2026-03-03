from random import randint
import repete
import repeteSelmini
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
    tamanho = [100, 1000, 10000]
    print('Comparação entre os métodos de Procura de repetição')
    print()
    
    for n in tamanho:
        print(f"Lista de tamanho {n}: ")
        lista = gerar_lista(n)
        tempo_Selmini = medir_tempo(repeteSelmini.pesquisar, lista)
        tempo_eu = medir_tempo(repete.eu, lista)
        print(f"Tempo Selmini {tempo_Selmini:.3f}")
        print(f"Tempo Eu {tempo_eu:.3f}")
        print("-" * 40)
        
if __name__ == "__main__":
    main()
    
    
    

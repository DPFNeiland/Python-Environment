import util
from random import randint

lista = [randint(0, 500) for _ in range(1000)]

print(util.BubbleSort(lista))




C = int(input())

lista = list(map(int,(input().split())))

resp = 0

for i in lista:
    if i == 1:
        resp += 1


print(f'{resp}')
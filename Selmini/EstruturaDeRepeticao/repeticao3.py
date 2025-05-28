
resp = "sim"

iterador = 0


while resp == "sim":

    num = int(input())

    for i in range(0,11):
        print(f'{num} * {i} == {num*i}')
    
    resp = str(input("Quer continuar? Sim ou não: "))

# for i in range(0,11):
#     print(f'{num} * {i} == {num*i}')
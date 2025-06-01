


lista = list(map(int, input().split()))

lista.sort()

if lista[0] + lista[1] > lista[2] and lista[2] + lista[0] > lista[1] and lista[1] + lista[2] > lista[0]:
    print("S")
    
elif lista[1] + lista[2] > lista[3] and lista[3] + lista[1] > lista[2] and lista[2] + lista[3] > lista[1]:
    print("S")

else:
    print("N")
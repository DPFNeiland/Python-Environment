

l1, l2, l3 = ([float(x) for x in input().split(" ")])

if(((l1 + l2 )> l3) and ((l3 + l1) > l2) and ((l2 + l3) > l1)):
    print("Existe um triângulo com esses lados.")
else:
    print("Triângulo inexistente.")
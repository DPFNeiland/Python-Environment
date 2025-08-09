def validar():
    return (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2)
        


def classificar():
    if lado1 == lado2 and lado2 == lado3:
        print("Triângulo equilátero")
        
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isóceles")
    
    else:
        print("Triângulo escaleno")

lado1 = float(input("Informe o primeiro lado --> "))
lado2 = float(input("Informe o segundo lado --> "))
lado3 = float(input("Informe o terceiro lado --> "))

if validar():
    classificar()
    
else:
    print("Os valores informados não formam um triângulo")
    
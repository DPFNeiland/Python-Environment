from cmath import sqrt



a = int(input("Digita o valor para o A: "))
b = int(input("Digita o valor para o B: "))
c = int(input("Digita o valor para o C: "))

if(a == 0):
    print("A == 0 resulta uma equação de primeiro grau")

if b**2 < 4*a*c:
    print("Delta menor que 0")
else: 

    x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2-4*a*c))/(2*a)
    
    print(f"Raiz 1: {x1:.2f}")
    print(f"Raiz 2: {x2:.2f}")

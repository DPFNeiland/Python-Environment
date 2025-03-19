
X = float(input("Digite o valor de X: "))

if(X >= -5 and X <= 5):
    print("Divisão por zero ou número imaginário.")
else:
    print(f"{((X-8)/(X**2-25)**(1/2)):.2f}")
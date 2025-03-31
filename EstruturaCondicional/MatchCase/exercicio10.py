



A, B, C = input('Digite o valor dos lados do triângulos: ').split()

A, B, C = float(A), float(B), float(C)

if A == B and B == C:
    print('Triângulo equilátero.')
    
elif A == B or A == C or B == C:
    print('Triângulo isóceles.')

else:
    print("triângulo escaleno.")
'''
NOTA = [float(0.0), float(0.0)]

for numero in NOTA:
    NOTA = float(input(f"Escreva sua nota da p{numero + 1}: "))


print(3,f"Sua média é {(NOTA)/2}")

'''
   # Codigo com uma variavel
MEDIA = float(0.0)

for numero in range(2):
    MEDIA += float(input(f"Escreva sua nota da p{numero + 1}: "))

print(f"Sua média é {(MEDIA)/2:.2f}")


'''
    :.2f
    : indica que vou formatar.
    O . e o divisor de águas que vai determinar a formatação antes
    ou depois da vírgula..
    F de float.
'''
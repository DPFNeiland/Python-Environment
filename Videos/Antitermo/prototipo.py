
inicio = 65
fim = 91

palavra = ["R", "U", "", "", ""]

Ntletras = ["E", "I", "F", "N", "A", "D"]

Tletras = ["O", "S"]

for i in range(inicio, fim):
    for j in range(inicio, fim):
        for k in range(inicio,fim):
            letra1 = chr(i)
            letra2 = chr(j)
            letra3 = chr(k)
        
            if (not (letra1 in Ntletras) and not (letra2 in Ntletras) and not (letra3 in Ntletras) and not (letra3 in Tletras)) and ((letra1 in Tletras) or (letra2 in Tletras)) :
                print(f"{chr(i)} {palavra[1]} {chr(j)} {palavra[3]} {letra3}"   )










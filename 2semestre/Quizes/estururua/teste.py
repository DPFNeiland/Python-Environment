dados = [3, 7, 0, -1, 7]
resultado = {}

for i in range(len(dados)):
    if dados[i] > 0:
        chave = f"v_{i}"
        if dados[i] not in resultado.values():
            resultado[chave] = dados[i]
        else:
            resultado[chave] = - dados[i]
    
    elif dados[i] == 0:
        continue
    
    else:
        resultado[f"neg_{i}"] = abs(dados[i])

print(resultado)
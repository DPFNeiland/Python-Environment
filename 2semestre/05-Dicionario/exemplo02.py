from random import choice

palavras_base = [
    "casa", "carro", "escola", "livro", "gato", "cachorro", "árvore", "flor", "porta", "janela",
    "mesa", "cadeira", "computador", "telefone", "estrada", "cidade", "praia", "rio", "montanha", "chuva",
    "sol", "lua", "estrela", "nuvem", "vento", "areia", "barco", "avião", "ônibus", "trem",
    "sapato", "camisa", "calça", "bola", "brinquedo", "papel", "caneta", "caderno", "quadro", "relógio",
    "pão", "leite", "arroz", "feijão", "fruta", "verdura", "doce", "bolo", "suco", "água"
]

lista = [choice(palavras_base) for _ in range(9999)]


jaUsadas = []
resul = []
vogais = [{'a': 0}, {'e': 0}, {'i': 0}, {'o': 0}, {'u': 0}]
i = 0

for palavra in lista:

    if not palavra in jaUsadas:
        jaUsadas.append(palavra)
        resul.append({"Palavra": palavra, "Qtd": lista.count(palavra)})
        
        vogais[0]["a"] += (palavra.count('a') + palavra.count('ã') + palavra.count('á') +  palavra.count('â')) * resul[i].get("Qtd")
        vogais[1]["e"] += (palavra.count('e') + palavra.count('é') + palavra.count('ê'))* resul[i].get("Qtd")
        vogais[2]["i"] += (palavra.count('i') + palavra.count('í')) * resul[i].get("Qtd")
        vogais[3]["o"] += (palavra.count('o') + palavra.count('ó') + palavra.count('ô') + palavra.count('õ'))  * resul[i].get("Qtd")
        vogais[4]["u"] += (palavra.count('u') + palavra.count('ú')) * resul[i].get("Qtd")
        i += 1

print(vogais)    
    
for palavraEqtd in resul:
    print(f"{palavraEqtd.get("Palavra")}: {palavraEqtd.get("Qtd")}")



'''
    Criando um dicionário:
'''

# Usando chaves e valores
meu_dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

outro_dicionario = dict(nome="Bob", idade=30, cidade="Rio de Janeiro")

print(meu_dicionario["nome"])
# Alice

print(meu_dicionario.get("profissão"))
# None

meu_dicionario["profissão"] = "Engenharia"
meu_dicionario["idade"] = 26 #atualiza o valor

del meu_dicionario["cidade"] # Remove a chave 'cidade'
profissao = meu_dicionario.pop("profissão") # Remove e retorna o valor associoado à chave "profissão"

print(meu_dicionario.keys())
print(meu_dicionario.values())
print(meu_dicionario.items())

meu_dicionario = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

for chave in meu_dicionario:
    print(chave)
    
for valor in meu_dicionario.values():
    print(valor)
    
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
    
dicionario = {"banana": 3, "maçã": 4, "laranja": 2, "pera": 1}

for chave in sorted(dicionario):
    print(f"{chave}: {dicionario[chave]}")
# banana: 3
# laranja: 2
# maçã: 4
# pera: 1
# Ordem alfabética das chaves

notas_alunos ={
    "Alice": [8.5, 7.0, 9.0],
    "Bob": [6.0, 7.5, 8.0],
    "Charlie": [9.5, 8.5, 7.0]
}

print(notas_alunos["Alice"])
# [8.5, 7.0, 9.0]

notas_alunos["Bob"].append(9.0)
print(notas_alunos["Bob"])
# [6.0, 7.5, 8.0, 9.0]


for aluno, notas in notas_alunos.items():
    media = sum(notas) / len(notas)
    print(f"Média de {aluno}: {media:.2f}")
    
# Média de Alice: 8.17
# Média de Bob: 7.62
# Média de Charlie: 8.33
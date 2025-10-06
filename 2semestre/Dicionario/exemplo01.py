
lista = []

for i in range(2):
    ra = int(input("RA: "))
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    lista.append({'ra': ra,  'nome': nome, 'nota':nota})
    print()
    
# quantidade de alunos que estão com nota acima da média

MEDIA = 7
total = 0
for i in range(len(lista)):
    aluno = lista[i]

    if aluno.get("nota") > MEDIA:
        total += 1

MEDIA = 7
total = 0
for aluno in lista:
    if aluno.get("nota") > MEDIA:
        total += 1
        
        
print(total)
print(lista)
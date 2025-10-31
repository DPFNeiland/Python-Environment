
alunos = [{'nome': 'A', 'RA': 1, 'Curso': 'SI'},{'nome': 'b', 'RA': None, 'Curso': 'SI'}]

for i in range(len(alunos)):
    print(f'Nome: {alunos[i].get("nome")}')
    print(f'Registro acadêmico: {alunos[i].get("RA")}')
    print(f'Curso: {alunos[i].get("Curso")}')
    # print(f'Curso: {alunos[i]['Curso']}') tá errado porque ele confunde os '' do formated string
    # do '' da tupla
    
    print()



aluno = -1

while not aluno >= 1:
    aluno = int(input('Informe a quantidade de alunos (valor válido) que irão votar: '))

favor = 0
contra = 0

for i in range (1, aluno + 1):
    voto = int(input('Você é contra ou a favor da criação da estação de bicicletas? A favor - 1 | Contra - 2 --> '))
    
    while voto < 1 or voto > 2:
        print('Por favor insira um dos valores indicados.')
        voto = int(input('Você é contra ou a favor da criação da estação de bicicletas? A favor - 1 | Contra - 2 --> '))
        
    match voto:
        case 1:
            favor += 1
        case 2:
            contra += 1
            
    porcent_favor = favor / aluno * 100
    
print(f'A quantidade de votos a favor é:{porcent_favor: .2f}%')
print(f'A quantidade de votos contra é de:{100 - porcent_favor: .2f}%')
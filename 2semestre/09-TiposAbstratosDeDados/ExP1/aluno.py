class Aluno:


    # construtor
    def __init__(self, nome = '', ra = 0, nota1 = 0, nota2 = 0):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
    
    # método para calcular e retornar a média simples
    def calcular_media(self) -> float:
        return (self.nota1+self.nota2)/2
    
    # método para retornar a situação do aluno (aprovado ou reprovado)
    def situacao(self) ->  str:
        media = self.calcular_media()
        if media >= 7.0:
            return "APROVADO"
        return "REPROVADO"
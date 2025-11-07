

def LerDados() -> list[tuple]:
    Dados = []
    
    n = int(input("Digite a quantidade de dias de leitura: "))

    for _ in range(n):
        dia, minima, maxima = str(input()).split()
        
        Dados.append((
            dia, minima, maxima
        ))
        
    return Dados

def FuncA(DadosDoDia: tuple) -> float:
    '''
    Implementa uma função para calcular a amplitude do dia. 
    A função deverá receber uma tupla (data, tmin, tmax) e 
    retornar a amplitude térmica do dia (tmax – tmin).
    '''
    
    return float(DadosDoDia[2]) - float(DadosDoDia[1])

def FuncB(Dados: list[tuple]) -> list[tuple]:
    '''
    Implementa uma função que receba a lista de tuplas e 
    retorne uma lista de tuplas no formato (data, media_dia, 
    amplitude), onde media_dia = (tmin + tmax)/2.
    '''
    novo_formato = []
    
    for dadosDoDia in Dados:
         novo_formato.append((
            dadosDoDia[0],
            (float(dadosDoDia[1]) + float(dadosDoDia[2]))/2,
            FuncA(dadosDoDia)
         ))
    
    return novo_formato

def FuncC(Dados: list[tuple]) -> list[str]:
    '''
    Implementa uma função que receba a lista do de tuplas no 
    formato (data, media_dia, amplitude) e retorne a data em 
    que houve a maior amplitude registrada.
    '''
    maiorAmplitude = -1
    listaDias = []
    
    for dadosDoDia in Dados:
        if dadosDoDia[2] > maiorAmplitude:
            maiorAmplitude = dadosDoDia[2]
            listaDias = []
                        
        if dadosDoDia[2] == maiorAmplitude:
            listaDias.append(dadosDoDia[0])
    
    return listaDias

def main():
    
    Dados = LerDados()
    
    dadosLimpos = FuncB(Dados)
    print(dadosLimpos)
    
    print(FuncC(dadosLimpos))


if __name__ == "__main__":
    main()
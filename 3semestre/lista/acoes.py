from collections import deque

fila = deque()

def vender_acoes(qtd: int, valorcada: float):
    total = 0

    menos = 0
    for acao in fila:
        if acao[1] <= qtd:
            total += acao[1] * (valorcada  - acao[2])
            qtd -= acao[1]
            menos += 1

        elif acao[1] > qtd:
            total += (qtd) * (valorcada - acao[2])
            acao[1] -= qtd

    for _ in range(menos):
        fila.popleft()

    return total

def main1():
    fila.append(['A', 100, 20])
    fila.append(['B', 20, 24])
    fila.append(['C', 200, 36])

    print(vender_acoes(150, 30))

    print(fila)


def vender_acoes_Selmini(transacao) -> float:
    fila = deque()
    montante = 0

    for t in transacao:
        tipo = t[0]

        if tipo == 'C':
            qtd = t[1]
            valor = t[2]
            fila.append((qtd, valor))
        
        elif tipo == 'V':
            qtd_venda = t[1]
            valor_venda = t[2]

            while qtd_venda > 0:
                lote = fila[0]
                if lote[0] <= qtd_venda:
                    montante += lote[0] * (valor_venda - lote[1])
                    qtd_venda -= lote[0]
                    fila.popleft()
                
                else:
                    lote[0] -= qtd_venda
                    montante += qtd_venda * (valor_venda - lote[1])
                    qtd_venda = 0

    return montante


def main2():
    transacao = [('C', 100, 20),
                 ('C', 20, 24),
                 ('C', 200, 36),
                 ('V', 150, 30)]
    
    montante = vender_acoes_Selmini(transacao)
    print(f'Montante R$ {montante:.2f}')

if __name__ == "__main__":
    main2()
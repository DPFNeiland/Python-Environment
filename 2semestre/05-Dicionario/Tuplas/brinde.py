
#  Implemente uma função em Python que recebe uma lista de tuplas, onde cada 
# tupla representa um intervalo numérico [𝑎𝑎, 𝑏𝑏], com 𝑎𝑎 ≤ 𝑏𝑏. A função deve 
# realizar as seguintes operações:

lista = [(2,4), (1,3), (7, 10), (3, 5)]

#  a) unir intervalos que se sobrepõem: se dois intervalos [𝑎𝑎, 𝑏𝑏] e [𝑐𝑐, 𝑑𝑑] se 
# sobrepõem (ou seja, 𝑏𝑏 ≥ 𝑐𝑐), eles devem ser unidos em um único intervalo.

def Unir_Intervalos(lista: list) -> tuple:

    nova_lista = []
    
    atual = lista[0]
    
    for i in range(1, len(lista)):
        
        tupla = lista[i]
        x2, y2 = tupla   

        xAtual, yAtual = atual

        
        if  x2 >= xAtual and x2 <= yAtual:
            atual = (min(xAtual,x2), max(yAtual, y2))
        else:
            nova_lista.append(atual)
            atual = (lista[min(i+1,len(lista) - 1)])
    
    nova_lista.append(atual)
    
    return nova_lista

    
#  b) contar o número total de intervalos resultantes.
def Contar_Intervalos(lista: list) -> int:
      
    return len(lista)


#  c) Retornar a soma total do comprimento de todos os intervalos resultantes.
def Contar_Comprimento(intervalos: list) -> int:
    
    soma = 0
    
    for intervalo in intervalos:
        x, y = intervalo

        soma += y - x + 1
        
    return soma

def main():
    lista_organizada = lista.sort()
    
    print(lista_organizada)
    
    nova_lista = Unir_Intervalos(lista)
    
    #  a) unir intervalos que se sobrepõem: se dois intervalos [𝑎𝑎, 𝑏𝑏] e [𝑐𝑐, 𝑑𝑑] se 
    # sobrepõem (ou seja, 𝑏𝑏 ≥ 𝑐𝑐), eles devem ser unidos em um único intervalo.
    print(nova_lista)
    
    #  b) contar o número total de intervalos resultantes.
    print(Contar_Intervalos(nova_lista))
    
    #  c) Retornar a soma total do comprimento de todos os intervalos resultantes.
    print(Contar_Comprimento(nova_lista))
    
    
if __name__ == "__main__":
    main()
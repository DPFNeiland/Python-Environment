


def mochilaInsana(itens: list[dict], capacidade: int, aux = -1):
    global valores
    
    if capacidade == 0:
        return 0
    
    for i in range(len(itens)):
        val_anterior = valores[capacidade - 1]
        val_atual = 0
        
        if itens[i].get("peso") <= capacidade and aux != i:
            val_atual = itens[i].get("valor") + mochilaInsana(itens, capacidade - itens[i].get("peso"), i)
            
        valores[capacidade-1] = max(val_anterior, val_atual)
    
    return valores[capacidade-1]
        


def main():
    itens = [
        {"nome": "violão", "valor": 1500, "peso": 1},
        {"nome": "notebook", "valor": 2000, "peso": 3},
        {"nome": "rádio", "valor": 3000, "peso": 4},
    ]
    capacidade = 5
    
    # itens = [
    #     {"valor": 22, "peso": 2},
    #     {"valor": 72, "peso": 17}, 
    #     {"valor": 44, "peso": 23},      
    #     {"valor": 31, "peso": 24},
    # ]
    # capacidade = 26

    global valores
    
    valores = [0] * capacidade
    
    print(mochilaInsana(itens, capacidade))

if __name__ == "__main__":
        main()
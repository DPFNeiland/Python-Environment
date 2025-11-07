

def lerSequenciasDNA() -> list:
    n = int(input("Digite quantas análises entre pai e filho deseja fazer: "))
    listaDNA = []


    for _ in range(n):
        pai = str(input("Sequência de DNA do pai: "))
        filho = str(input("Sequência de DNA do filho: "))
        
        if (len(pai) <= 1 or len(filho) <= 1) or (len(pai) != len(filho)):
            print("SEQUÊNCIAS DE TAMANHO INVÁLIDO")
        
        else:
            listaDNA.append({
                "pai": pai,
                "filho": filho
            })

    return listaDNA

def VerificarCompatilidade(listaDNA: dict) -> bool:
    
    
    letraCompativel = 0
    letraNCompativel = 0
    
    sequenciaDNApai = listaDNA["pai"]
    sequenciaDNAfilho = listaDNA["filho"]
    
    metade = len(sequenciaDNAfilho) // 2
    if len(sequenciaDNAfilho) % 2 == 1:
        metade += 1

    
    for i in range (metade, len(sequenciaDNAfilho)):
        if sequenciaDNApai[i] == sequenciaDNAfilho[i]:
            letraCompativel += 1
        letraNCompativel += 1
    
    print(f"{letraCompativel/letraNCompativel*100:.2f}%")
    if letraCompativel/letraNCompativel >= 0.70:
        return True
    return False

def main(): 
    listaDNA = lerSequenciasDNA()
    
    for sequencia in listaDNA:
        print("pai: " + sequencia["pai"])
        print("filho: " + sequencia["filho"])
        if VerificarCompatilidade(sequencia):
            print("POTENCIAL PAI-FILHO")
        else: 
            print("NÃO COMPATÍVEL")
        
        
if __name__ == "__main__":
    main()
# 2. (1,5) Um vetor A contém n inteiros retirados do intervalo [0, 4n], com repetições  permitidas. 
# Implemente um programa em Python contendo uma função para determinar o valor inteiro k  
# que ocorre com mais frequência.  

# Requisitos 
# a) O programa deve receber como entrada um array contendo n inteiros retirados do intervalo 
# [0, 4n]. Os valores deverão ser informados via terminal e não podem estar fora do intervalo 
# especificado. O valor de n também deverá ser informado via teclado. 
# b) O programa deve imprimir no terminal o elemento com frequência máxima e sua frequência 
# associada. 
# c) Caso todos os valores apresentam a mesma frequência imprimir a mensagem "Todos os 
# valores apresentam a mesma frequência". 
# d) O programa não pode usar recursividade.


def calcular_valor_mais_visto(vector: list[int]):
    qtd = {}

    for ele in vector:
        if ele in qtd:
            qtd[ele] += 1
            
        else:
            qtd[ele] = 1
            
    m_qtd = max(qtd.values())
    
    m_ele= [k for k, v in qtd.items() if v == m_qtd]

    if len(m_ele) == len(qtd):
        return("Todos os valores apresentam a mesma frequência")
    
    elif len(m_ele) == 1:
        valor_k = m_ele[0]
        return(f"Elemento com frequência máxima: {valor_k}\nFrequência associada: {m_qtd}")
    else:
        return("Existe mais de 1 valor com a mesma frequência")


def main():
    n = int(input())
    v = []
    for _ in range(n):
        v.append(int(input()))
    
    print(calcular_valor_mais_visto(v))


if __name__ == "__main__":
    main()


# Por haver apenas um for, a complexidade desse algoritmo é O(n) 

# Possíveis entradas:
# 7
# 5
# 5
# 5
# 3
# 3
# 4
# 4


# 8
# 2
# 2
# 2
# 2
# 3
# 3
# 3
# 3

# 9
# 2
# 2
# 2
# 2
# 3
# 3
# 3
# 3
# 1


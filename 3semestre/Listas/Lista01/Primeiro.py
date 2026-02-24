# 1. (1,5) Implemente um programa em Python contendo uma função que verifique se um vetor de 
# inteiros contém pelo menos um elemento A[i] que seja a soma de dois valores anteriores no 
# próprio vetor. Ou seja, seu programa deve identificar se existem índices j e k (j < i e k < i) tais que: 
# A[i] = A[j] + A[k]. Após a implementação do seu algoritmo, descreva qual a ordem de 
# complexidade em notação O da função responsável por fazer a verificação (coloque essa 
# informação como comentário no início do código). 

# Requisitos 
# a) O programa deve receber como entrada um array contendo n inteiros. Os valores deverão 
# ser informados via terminal. 
# b) O algoritmo deve verificar, para cada elemento A[i] (a partir do terceiro), se ele pode ser 
# obtido como soma de dois elementos anteriores. 
# c) O programa deve imprimir "Existe um elemento que é a soma de dois anteriores." caso 
# encontre tal valor, ou "Nenhum elemento é a soma de dois anteriores." caso contrário. 
# d) O programa não pode usar recursividade. 

# Exemplo de Entrada: A = {3, 8, 4, 12, 7, 15}; // 15 = 8 + 7 
# Exemplo de Saída: Existe um elemento que é a soma de dois anteriores. 


# Well, exercício "simples" e tenho 1 ideia que chama mais atenção:
# armazenar todas as somas possíveis num set e verificando se existe essa soma.

# A função verificar_soma_2_ideia1() tem a datação O(n^2) por conta do for aninhado para 
# adicionar todas as somas possíveis. Por mais que minhas tentativas de otimizar ele
# para uma complexidade menor utilizando if's, consigo evitar processamento desnecessário.
def verificar_soma_2_ideia1(vector: list[int]):
    val = set() 
    n = len(vector)
    
    val.add(vector[0] + vector[1])

    for i in range(2, n):
        if vector[i] in val:
            return "Existe um elemento que é a soma de dois anteriores."
        
        for j in range(0, i):
            val.add(vector[i]+vector[j])
            if vector[i] in val:
                return "Existe um elemento que é a soma de dois anteriores."
        
    return "Nenhum elemento é a soma de dois anteriores."

def main():
    n = int(input())
    v = []
    for _ in range(n):
        v.append(int(input()))

    print(verificar_soma_2_ideia1(v))

if __name__ == '__main__':
    main()


# Por mais que minhas tentativas de otimizar ele para uma complexidade menor utilizando if's, 
# consigo evitar processamento desnecessário.

# Tenho um sentimento de intuição de que dá para realizar com O(n*logn), mas provavelmente 
# é utilizando recursividade... Ou apenas um sentimento de que sempre é possível melhorar.

# [...] "No me arrepiento, porque aquel momento lo llevo grabado en mi pensamiento"
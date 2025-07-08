


def mostrar_Binario(x: int):
    for i in range(31,-1,-1):
        if(x&(1<<i) != 0):
    # x AND (...0000001 deslocado i vezes para a esquerda)
    # Por exemplo: quando i = 5, então ele desloca esse 1 
    # 5 vezes pra esquerad -> (32) base10 -> (100000) base2
    # quando x = (50) base10 -> (00110010) base2, fazendo um AND 
    # lógico, é notável que o resultado (00100000) base2 é
    # diferente de 0, logo, bit 1.
    # mas se o i = 3, desloca - se o 1 quatro vezes pra 
    # esquerda (1000) base2, fazendo o AND lógico com o 
    # (00110010) base2, tu tens como resultado 0, logo,
    # é bit zero 
            print("1", end="")
        else:
            print("0", end="")
    print()
    
x = 50            
mostrar_Binario(x)

# Agora que vem o BOOOOOOOOOOOM!!!☠☠
# Para calcular o negativo do número, tu faz um NOT
# em cada bit do número, e no fim, tu soma em 1 no final.
# E.g: (50) base10 = (00000000000000000000000000110010) base2
# NOT (00000000000000000000000000110010) base2 = (11111111111111111111111111001101) base2
# (11111111111111111111111111001101) base2 + (00001) base2 = 11111111111111111111111111001110

mostrar_Binario(-x) 




a, b = 10, 13

print()
print("AND:", end=" ")
mostrar_Binario(a&b)

print("OR:", end=" ")
mostrar_Binario(a|b)

print("XOR:", end=" ")
mostrar_Binario(a^b)

print("NOT a:", end=" ")
mostrar_Binario(~a)

print("NOT b:", end=" ")
mostrar_Binario(~b)

print("SHIFT Left 1 bit:", end=" ")
mostrar_Binario(a<<1)

print("SHIFT Right 1 bit:", end=" ")
mostrar_Binario(a>>1)

print(a>>1) # Divisão por 2
print(a<<1) # Multiplicação por 2




def Inserir_Valor_Em_Um_Conjunto(A: int, x: int):
    return A | ( 1<< x)
# A: 10000101
#    | 100000  
# A: 10100101
# x: 5


def Remover_Valor_Em_Um_Conjunto(A: int, x: int):
    return A & (~(1<< x))
# A: 10000101
# 7= 10000000
#~7= 01111111
# A:&10000101
#    00000101
# A: 10100101
# x: 7

def Calcular_Intersecao(A: int, B: int):
    return A&B

def Calcular_Uniao(A: int, B: int):
    return A|B

def Calcular_Complemento(A: int):
    return ~A


a, b = 0, 0
a = Inserir_Valor_Em_Um_Conjunto(a, 1)
a = Inserir_Valor_Em_Um_Conjunto(a, 3)
a = Inserir_Valor_Em_Um_Conjunto(a, 4)

b = Inserir_Valor_Em_Um_Conjunto(b, 4)
b = Inserir_Valor_Em_Um_Conjunto(b, 5)

mostrar_Binario(a)
mostrar_Binario(b)

mostrar_Binario(Calcular_Intersecao(a,b))



# Num = int(input())

# resp = 1

# for i in range(2, Num+1 ):
    
#     print(resp)
    
#     if i%2 == 0:
#         resp -= 1/i
        
#     else:
#         resp += 1/i
        
# print(resp)


n = int(input("Informe o valor n maior que zero: "))
y = 0
sinal = 1

if n <= 0:
    print("Valor de n deve ser MAIOR QUE zero")

else:
    for denominador in range(1, n+1):
        y = y + 1 /denominador * sinal
        
        sinal *= -1
        
    print(f"y = {y}")
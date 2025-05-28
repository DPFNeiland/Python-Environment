

A, B = 1, 1


while A != 0 and B != 0:
    lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    A, B = input().split()
    
    A = int(A)
    B = int(B)
    
    if A == 0 and B == 0:
        break
    
    for string in range(A, B + 1):
        
        for char in str(string):
            lista[int(char)] += 1
            
    for num in lista:
        print(num, end=" ")
    print()
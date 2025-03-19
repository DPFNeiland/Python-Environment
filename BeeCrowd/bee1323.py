

number = 1

def Feyman(n):
    if(n == 1):
        return 1
    return n*n + Feyman(n-1)

while number != 0:
    number = int(input())
    if(number == 0):
        break
    print(Feyman(number))
    
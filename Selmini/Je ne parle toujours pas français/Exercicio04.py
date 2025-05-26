x = 1
y = 0

sum = 0

x = x + y

print('Os números pares da sequência de Fibonacci são:')

while x < 4000000:
    x, y = x + y, x
    if x % 2 == 0:
        sum += x
        print(x, end=' ')
        
print()
print()

print('A soma dos números pares da sequência de Fibonacci é: ')
print(sum, end=' ')
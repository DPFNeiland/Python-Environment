


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


# Conta quantas 'apple' tem.
print(fruits.count('apple'))

# Conta quantas 'tangerine' tem.
print(fruits.count('tangerine'))

# Acha o item na lista mais próximo do indice zero
print(fruits.index('banana'))

# Acha o item na lista 'banana' mais próximo a partir do zero
print(fruits.index('banana', 4))


fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())
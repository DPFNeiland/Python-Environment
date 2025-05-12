



# print(f'{(8>3 and (4 != 3))}')

# print(f'{((4+2) <= 10) or (33 != (10*3))}')

# print(f'{not(4>2) or (4>2)}')

# print(f'{not(4>2) and (4 > 2)}')



# a = int(input("Valor de a: "))
# b = int(input("Valor de b:"))
# c = int(input("Valor de c:"))
# d = int(input("Valor de d:"))
# e = f = g = 0

# if a > b and a > c and a > d:
#     e = a

# elif b > a and b > c:
#     e = b
    
# else:
#     e = c
    
    
# if a > b or c > d:
#     g = g + 1
    
# else:
#     f = f + 1
    
# if b < c:
#     e = e + 2
#     f = f + 2
    
# if d > a:
#     e = e + 3
#     f = f + 3
    
# g = g + 3

# print(f'a: {a}')
# print(f'b: {b}')
# print(f'c: {c}')
# print(f'd: {d}')
# print(f'e: {e}')
# print(f'f: {f}')
# print(f'g: {g}')



# a = 10
# b = 5
# c = 15
# d = 4

# if a > b or c > d:
#     a = b + c
#     c = d + b
    
# else:
#     c = a + d
    
# if c < a and b % c == 0:
#     a = d - b
#     b = c + a
#     d = -a
    
# else:
#     d = d - c
#     a = d + b
    
# if b < a or (c > a and d < b):
#     c = a + b
#     a = b + c
#     b = c - a
    
# if b > a:
#     c = c + a
    
# elif c < a:
#     b = a - c

# elif d > b:
#     a = b + d
  
a = 10
b = 5
c = 15
d = 4

if a > b or c > d:
    a = b + c
    c = d + b
else:
    c=a+ d

if c < a and b % c == 0:
    a = d - b
    b = c + a   
    d = - a
else :
    d = b - c
    a = d + b



if b < a or ( c > a and d < b ) :
    c= a + b
    a = b + c
    b = c - a


if b > a:
    c =c+ a
elif c < a:
    b = a - c
elif d > b:
    a = b + d


print(a)
print(b)
print(c)
print(d)
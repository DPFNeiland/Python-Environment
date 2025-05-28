a = int(input("Valor de a: "))
b = int(input("Valor de b:"))
c = int(input("Valor de c:"))
d = int(input("Valor de d:"))
e = f = g = 0

if a > b and a > c and a > d:
    e = a
elif b > a and b > c:
    e = b
else:
    e = c
    
    
if a > b or c > d:
    g = g + 1
else:
    f = f + 1

if b < c:
    e = e + 2
    f = f + 2
    
if d > a:
    e = e + 3
    f = f + 3
    
g = g + 3

print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')
print(f'd: {d}')
print(f'e: {e}')
print(f'f: {f}')
print(f'g: {g}')
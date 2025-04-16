



a = 10
b = 5
c = 15
d = 4
if a > b or c > d:
    a = b + c
    c = d + b
else:
    c = a + d
    
if c < a and b % c == 0:
    a = d - b
    b = c + a
    d = -a
else:
    d = b - c
    a = d + b
    
if b < a or (c > a and d < b):
    c = a + b
    a = b + c
    b = c - a
    
if b > a:
    c = c + a
elif c < a:
    b = a - c
elif d > b:
    a = b + d
    
print(a)
print(b)
print(c)
print(d)
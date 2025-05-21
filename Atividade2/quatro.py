






x1 = 1
x2 = 2

while x2 <= 4000000:
    aux = x1 + x2
    
    if x1 + x2 > 4000000:
        break
    
    x1, x2  = x2, x1 + x2
    
    print(x2, end=" ")
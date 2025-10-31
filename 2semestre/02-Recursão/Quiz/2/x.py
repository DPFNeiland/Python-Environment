

def x(a, b):
    if a == 0 or b == 0:
        return 0
    
    if a == b:
        return 1 + x(a -1, b - 1)
    
    if a != b:
        return min(x(a, b-1), x(a-1,b))
    
    
print(x(5,0))
print(x(8,8))
print(x(10,12))
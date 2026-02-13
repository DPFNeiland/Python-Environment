

def misteriosa(a):
    if a < 1: return -1
    if a == 1: return 2
    return misteriosa(a - 1) * misteriosa(a - 2)

print(misteriosa(1))
print(misteriosa(3))
print(misteriosa(4))


def f(a, b):
    if b == 0:
        return a
    return f(b, a %b)

print(f(30,21))
def fib_mod(n, m):
    # Encontra período de Pisano
    pisano = [0, 1]
    for i in range(2, m * m + 1):
        pisano.append((pisano[-1] + pisano[-2]) % m)
        if pisano[-2] == 0 and pisano[-1] == 1:
            pisano.pop()
            pisano.pop()
            break
    p = len(pisano)
    return pisano[n % p]

while True:
    try:
        n, m = map(int, input().split())
        fn = fib_mod(n, 2_000_000_000)  # só para exemplo, ajustar aqui
        print(fib_mod(fn, m))
    except EOFError:
        break

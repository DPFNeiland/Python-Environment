class Misterio:
    def __init__(self, v, nxt=None):
        self.v = v
        self.nxt = nxt


def transformar(a: Misterio, b: Misterio):
    a.v += 1
    b = Misterio(a.v, a)
    a.nxt = b
    return a, b


if __name__ == "__main__":
    n1 = Misterio(2)
    n2 = Misterio(3)

    x, y = transformar(n1, n2)

    n2.nxt = x
    y = n1
    n1.v = 10

    p = x
    s = []

    for _ in range(3):
        s.append(p.v)
        p = p.nxt

    print(s)
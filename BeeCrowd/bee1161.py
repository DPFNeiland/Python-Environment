


def fatorial(n):
    if n == 1 or n == 0:
        return 1
    return n*fatorial(n-1)


while(True):
    try:

        m, n = ([int(x) for x in input().split(" ")])

        print(fatorial(m)+fatorial(n))
    
    except EOFError:
        break
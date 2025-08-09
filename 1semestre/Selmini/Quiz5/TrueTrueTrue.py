


def funcaoDoFernando(a,b,c):
    x = (a and b) and ((c or a or b) or (not(a) and c))
    print( x)

funcaoDoFernando(True, True, False)
funcaoDoFernando(False, True, True)
funcaoDoFernando(False, True, False)
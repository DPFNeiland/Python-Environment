
def ZerotoNull(Resp):
    resp = "".join([char if char in "0" else "" for char in Resp])

    print(resp)

Ni = 1
Mi = 1

while Ni != '0' and Mi != '0':
    Ni, Mi = [str(x) for x in input().split()]

    if Ni != '0' and Mi != '0':
        
        Resp = str(int(Ni) + int(Mi))

        Resp.replace('0','1')
        
        ZerotoNull(Resp )
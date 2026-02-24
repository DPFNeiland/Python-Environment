
class Lua:
    def __init__(self, x: int) -> None:
        self.x = x
    
def alcancar_a_lua(d: dict, p: Lua) -> None:
    d['a'] = p
    d['b'] = Lua(p.x)
    p.x = 7
    d['b'].x = 3


d = {}
p = Lua(1)
alcancar_a_lua(d, p)

print(d['a'].x)
print(d['b'].x)
print(p.x)

# class Dozens:
#     def __init__(self):
#         self.dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# if __name__ == "__main__":
#     da : list[Dozens] = []
#     da.append(Dozens())
#     d = Dozens()
#     da.append(d)
#     d = None
#     da[1] = None
#     # faça algo

# 5,2           5,5
# 


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
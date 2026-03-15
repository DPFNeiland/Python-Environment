class No:
    def __init__(self, dado):
        self.dado = dado
        self.ant: No = None
        self.pos: No = None


 class Lista:
    def __init__(self):
        self.tamanho: int = 0
        self.inicio: No = None
        self.pos: No = None
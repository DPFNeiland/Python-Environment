
class No:
    def __init__(self, dado: any):
        self.dado: any = dado
        self.esq: No = None
        self.dir: No = None
        
class ABB:
    def __init__(self):
        self.raiz: No = None
        

    # método para inserir um dado na árvore binária de busca
    def inserir(self, dado: any):
        self.raiz = self._inserir(self.raiz, dado)
        
    # método recursivo para inserir um dado na árvore
    def _inserir(self, no: No, dado: any):
        if no is None:
            return No(dado)
        
        if dado > no.dado:
            no.dir = self._inserir(no.dir, dado)
        
        if dado < no.dado:
            no.esq = self._inserir(no.esq, dado)
        
        return no
    
    # método para fazer o percuso em ordem
    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    # método auxiliar recursivo para fazer o percuso em ordem
    def _em_ordem(self, no: No, resultado: list[any]):
        if no is None:
            return
        
        self._em_ordem(no.esq, resultado)
        resultado.append(no.dado)
        self._em_ordem(no.dir, resultado)        
        
        return resultado
    
    # método para remover um elemento da árvore
    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)
    
    def _remover(self, no: No, valor: any):
        if no is None:
            return None
        
        if valor < no.dado:
            no.esq = self._remover(no.esq, valor)
            
        
        if valor > no.dado:
            no.dir = self._remover(no.dir, valor)
        
        else:
            # caso 1 - O nó não tem filhos (é uma folha)
            if no.esq is None and no.dir is None:
                return None
            
            # caso 2 - o nó só tem um filho 
            if no.esq is None:
                return no.dir
            
            if no.dir is None:
                return no.esq
            
            # caso 3 -> o nó te dois filhos
            
            sucessor: No = self.buscar_menor(no.dir)
            no.dado = sucessor.dado
            no.dir = self._remover(no.dir, sucessor.dado)
    
    def buscar_menor(self, no):
        atual = no
        
        while no.esq is not None:
            atual = atual.esq
            
        return no
        
    
if __name__ == "__main__":
    print('*' * 85)
    arvore = ABB()
    
    arvore.inserir(15)
    arvore.inserir(7)
    arvore.inserir(10)
    arvore.inserir(25)
    
    print(arvore.em_ordem())
    
    arvore.remover(20)
    print(arvore.em_ordem())
    
    arvore.remover(20)
    print(arvore.em_ordem())

# classe para representar os nós da árvore
class No:
    def __init__(self, valor):
        self.valor  = valor
        self.esq    = None   
        self.dir    = None   
        self.altura = 1      # altura do nó (folha começa com 1)

    def __repr__(self):
        return f"No({self.valor})"


# classe para representar a árvore AVL e suas operações
class AVL:
    def __init__(self):
        self.raiz = None

    # conjunto de métodos auxiliares
    def _altura(self, no):        
        if no is None:
            return 0 # None tem altura 0
        
        return no.altura

    def _atualizar_altura(self, no):        
        no.altura = 1 + max(self._altura(no.esq), self._altura(no.dir))

    def _fator(self, no):
        """
        Calcula o fator de balanceamento de um nó.
        Fator = altura(esq) - altura(dir)
          > 1  → pesado à esquerda → rotação à direita
          < -1 → pesado à direita  → rotação à esquerda
        """
        if no is None:
            return 0
        
        return self._altura(no.esq) - self._altura(no.dir)

    # métodos para realizar as rotações na árvore
    def _rotacao_direita(self, z):
        """
        Rotação simples à direita em torno do nó z.

              z                     y
             / \\                  / \\
            y   T4      →        x    z
           / \\                  / \\ / \\
          x   T3               T1 T2 T3 T4
         / \\
        T1  T2
        """
        y  = z.esq
        T3 = y.dir

        # rotaciona
        y.dir = z
        z.esq = T3

        # atualiza alturas (z primeiro, pois agora é filho de y)
        self._atualizar_altura(z)
        self._atualizar_altura(y)

        return y   # nova raiz da subárvore

    def _rotacao_esquerda(self, z):
        """
        Rotação simples à esquerda em torno do nó z.

            z                        y
           / \\                     / \\
          T1   y         →         z    x
              / \\                 / \\ / \\
             T2   x              T1 T2 T3 T4
                 / \\
                T3  T4
        """
        y  = z.dir
        T2 = y.esq

        # rotaciona
        y.esq = z
        z.dir = T2

        # atualiza alturas
        self._atualizar_altura(z)
        self._atualizar_altura(y)

        return y   # nova raiz da subárvore

    # método para realizar o rebalanceamento da árvores
    def _rebalancear(self, no):
        """
        Verifica o fator de balanceamento e aplica a rotação adequada.

        Há quatro casos possíveis de desbalanceamento:
          1. Esquerda-Esquerda  → rotação simples à direita
          2. Esquerda-Direita   → rotação dupla (esquerda no filho, direita na raiz)
          3. Direita-Direita    → rotação simples à esquerda
          4. Direita-Esquerda   → rotação dupla (direita no filho, esquerda na raiz)
          
          se vc quiser fazer essa seta que aparece no texto, basta colocar o caractere especial \u2192 
        """
        self._atualizar_altura(no)
        fb = self._fator(no)

        # caso 1: Esquerda-Esquerda
        if fb > 1 and self._fator(no.esq) >= 0:
            return self._rotacao_direita(no)

        # caso 2: Esquerda-Direita
        if fb > 1 and self._fator(no.esq) < 0:
            no.esq = self._rotacao_esquerda(no.esq)
            return self._rotacao_direita(no)

        # caso 3: Direita-Direita
        if fb < -1 and self._fator(no.dir) <= 0:
            return self._rotacao_esquerda(no)

        # caso 4: Direita-Esquerda
        if fb < -1 and self._fator(no.dir) > 0:
            no.dir = self._rotacao_direita(no.dir)
            return self._rotacao_esquerda(no)

        return no   # nó já balanceado

    # método para inserir um elemento na árvore AVL (lembrem-se que não há valores repetidos)
    def inserir(self, valor):        
        self.raiz = self._inserir(self.raiz, valor)

    # método auxiliar recursivo para fazer a inserção de um elemento
    def _inserir(self, no, valor):        
        if no is None:
            return No(valor)

        if valor < no.valor:
            no.esq = self._inserir(no.esq, valor)
        elif valor > no.valor:
            no.dir = self._inserir(no.dir, valor)
        else:
            return no   # duplicado, ignora

        # rebalancer na volta da recursão
        return self._rebalancear(no)

    # método para remover um elemento da árvore AVL
    def remover(self, valor):        
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, no, valor):
        if no is None:
            return None

        if valor < no.valor:
            no.esq = self._remover(no.esq, valor)
        elif valor > no.valor:
            no.dir = self._remover(no.dir, valor)
        else:
            if no.esq is None:
                return no.dir   
            
            if no.dir is None:
                return no.esq   

            # se tiver dois filhos: substitui pelo sucessor in-order (menor da subárvore direita)
            sucessor = self._minimo(no.dir)
            no.valor = sucessor.valor
            no.dir   = self._remover(no.dir, sucessor.valor)

        # rebalancear na volta da recursão
        return self._rebalancear(no)

    def _minimo(self, no):
        while no.esq is not None:
            no = no.esq
        return no

    # método para buscar um valor/elemento na árvore AVL
    def buscar(self, valor):        
        return self._buscar(self.raiz, valor)

    def _buscar(self, no, valor):
        if no is None:
            return False
        
        if valor == no.valor:
            return True
        
        if valor < no.valor:
            return self._buscar(no.esq, valor)
        
        return self._buscar(no.dir, valor)

    # métodos de percursos: são os mesmos utilizados para a implementação da árvore binária de busca
    def pre_ordem(self):
        """pré-ordem: Raiz → Esquerda → Direita."""
        resultado = []
        self._pre_ordem(self.raiz, resultado)
        return resultado

    def _pre_ordem(self, no, resultado):
        if no is None:
            return
        resultado.append(no.valor)
        self._pre_ordem(no.esq, resultado)
        self._pre_ordem(no.dir, resultado)

    def em_ordem(self):
        """em-ordem: Esquerda → Raiz → Direita (retorna valores crescentes)."""
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, resultado):
        if no is None:
            return
        self._em_ordem(no.esq, resultado)
        resultado.append(no.valor)
        self._em_ordem(no.dir, resultado)

    def pos_ordem(self):
        """pós-ordem: Esquerda → Direita → Raiz."""
        resultado = []
        self._pos_ordem(self.raiz, resultado)
        return resultado

    def _pos_ordem(self, no, resultado):
        if no is None:
            return
        self._pos_ordem(no.esq, resultado)
        self._pos_ordem(no.dir, resultado)
        resultado.append(no.valor)

    # métodos para calcular a altura da árvore e o fator de balanceamento
    def altura(self):        
        return self._altura(self.raiz)

    def fator_balanceamento(self, valor):        
        no = self._localizar(self.raiz, valor)
        
        if no is None:
            raise ValueError(f"Valor {valor} não encontrado na árvore.")
        
        return self._fator(no)

    def _localizar(self, no, valor):        
        if no is None:
            return None
        
        if valor == no.valor:
            return no
        
        if valor < no.valor:
            return self._localizar(no.esq, valor)
        
        return self._localizar(no.dir, valor)


# simulação da programa
if __name__ == "__main__":
    avl = AVL()

    # sequência crescente que degenera uma ABB comum
    valores = [10, 20, 30, 40, 50, 25]
    print("=== Inserindo valores ===")
    for v in valores:
        avl.inserir(v)
        print(f"  Inserido {v:>2} | altura da árvore: {avl.altura()}")

    print()
    print("=== Percursos ===")
    print(f"  Pré-ordem : {avl.pre_ordem()}")
    print(f"  Em-ordem  : {avl.em_ordem()}")
    print(f"  Pós-ordem : {avl.pos_ordem()}")

    print()
    print("=== Busca ===")
    print(f"  buscar(25) → {avl.buscar(25)}")
    print(f"  buscar(99) → {avl.buscar(99)}")

    print()
    print("=== Fator de balanceamento ===")
    for v in valores:
        print(f"  FB({v:>2}) = {avl.fator_balanceamento(v):>2}")

    print()
    print("=== Remoção ===")
    print(f"  Em-ordem antes : {avl.em_ordem()}")
    avl.remover(30)
    print(f"  Removido 30")
    print(f"  Em-ordem depois: {avl.em_ordem()}")
    print(f"  Altura após remoção: {avl.altura()}")
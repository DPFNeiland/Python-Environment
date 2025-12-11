
import util

def estranho(A):
    if len(A) <= 1:
        return A
    p = A[-1]
    G = [x for x in A[:-1] if x >  p]
    return estranho(G)

# L = [x for x in A[:-1] if x <= p]
# G = [x for x in A[:-1] if x >  p]

# estranho(G) + [p] + estranho(L)

A = [5, 3, 5, 2, 5, 4]

print(util.quicksort(A, 0, None))

print(A)
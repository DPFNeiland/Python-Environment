def eh_legal(mat):
    L = len(mat)
    C = len(mat[0])

    for i in range(1, L):
        for j in range(1, C):
            if mat[0][0] + mat[i][j] > mat[0][j] + mat[i][0]:
                return False
    return True


def eh_super_legal(mat):
    L = len(mat)
    C = len(mat[0])

    for l1 in range(L):
        for l2 in range(l1 + 1, L):
            for c1 in range(C):
                for c2 in range(c1 + 1, C):
                    sub = [linha[c1:c2 + 1] for linha in mat[l1:l2 + 1]]
                    if not eh_legal(sub):
                        return False
    return True


def maior_submatriz_super_legal(A):
    L = len(A)
    C = len(A[0])
    melhor = 0

    for l1 in range(L):
        for l2 in range(l1 + 1, L):
            for c1 in range(C):
                for c2 in range(c1 + 1, C):
                    sub = [linha[c1:c2 + 1] for linha in A[l1:l2 + 1]]

                    if eh_super_legal(sub):
                        area = (l2 - l1 + 1) * (c2 - c1 + 1)
                        if area > melhor:
                            melhor = area

    return melhor


L, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(L)]

print(maior_submatriz_super_legal(A))

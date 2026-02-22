


def feionacci(n: int):
    if n == 1:
        return 1
    return feionacci(n-1) * feionacci(n-1)

print(feionacci(4))
print(feionacci(5))
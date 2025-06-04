




D = int(input())
A = int(input())
N = int(input())


if N <= 15:
    diaria = D + ((N - 1)* A)
else:
    diaria = D + 14*A


total = ((32 - N))* diaria

print(total)
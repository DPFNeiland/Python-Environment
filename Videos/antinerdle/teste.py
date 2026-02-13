

# possible = [2, 4, 6, 7, 8, 0]
# n = len(possible)

# notPrim = [4,7,2]
# notSec = [2]

# resp = ['', '*', '7', '', '=', '', '', '4']


# for i in range(n):
#     if not possible[i] in notPrim:
#         for j in range(n):
#             if not possible[j] in notSec:
#                 for k in range(n):
#                     for l in range(n    ):
#                         if possible[i]* (70 + possible[j]) == possible[k] * 100 + possible[l] * 10 + 4:
#                             print(f"{possible[i]} * 7{possible[j]} = {possible[k]}{possible[l]}4")


possible = [4, 5, 6, 7, 0]
n = len(possible)

notSegu = [4]
notQuin = [7]

for i in range(n):
    for j in range(n):
        if not possible[j] in notSegu:

            for k in range(n):
                for l in range(n):
                    for m in range(n):
                        if not possible[l] in notQuin:
                            if possible[i] * (possible[j]*10 + possible[k]) == (possible[l] * 100 + possible[m] * 10):
                                print(f"{possible[i]}*{possible[j]}{possible[k]} = {possible[l]}{possible[m]}0")
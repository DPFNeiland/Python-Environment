

# letra A

# num = 2
# while num <= 50:
#     primo = False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             primo = True
#             break
#     if primo:
#         print(num, end=' ')
#     num += 1
    
# Saída: 4 6 8 9 10 12 14 15 16 18 20 21 22 24 25 26 27 28 30 32 33 34 35 36 38 39 40 42 44 45 46 48 49 50 

    
# Lebra B

# for num in range(2, 51):
#     primo = True
#     for i in range(2, num):
#         if num % i != 0:
#             primo = False
#     if primo:
#         print(num, end=' ')

# Saída: 2



# Letra C


# num = 2
# while num <= 50:
#     if num > 1:
#         for i in range(2, num+1):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=' ')
#     num += 1
    
    
    
for num in range(2, 51):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
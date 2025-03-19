

first = 8>3
second = 4 != 3

result = 8>3 and 4 != 3
    
print(f"{first} and {second} result: {result}")

first = (4 + 2 <= 10)
second = (33 != 10*3)

result = first or second

print(f"{first} or {second} result: {result}")

result = not(True)

print(result)

first = (not(4>2))
second = (4>2)

result = first or second

print(f"{first} or {second} result: {result}")

first = (not(4>2))
second = (4>2)

result = first and second

print(f"{first} and {second} result: {result}")
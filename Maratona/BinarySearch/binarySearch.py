
def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1
    
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        
        elif item < midpoint_value:
            end_index = midpoint - 1
            
        else:
            begin_index = midpoint + 1
            
    return None

# lista = [10,9,8,5,3,7,92,185,78,1,0,65]
lista = [0, 1, 3, 5, 7, 8, 9, 10, 65, 78, 92, 185]

item = int(input("Digite qualquer valor da lista: "))

print(binary_search(lista, item))
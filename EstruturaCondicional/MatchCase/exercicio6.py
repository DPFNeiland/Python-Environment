




val1, op, val2 = [str(x) for x in input().split()]

val1 = float(val1)

val2 = float(val2)

match op:
    case "+":
        print(f'{val1:.1f} {op} {val2:.1f} = {val1+val2:.1f}')
    
    case "-":
        print(f'{val1:.1f} {op} {val2:.1f} = {val1-val2:.1f}')
    
    case "*":
        print(f'{val1:.1f} {op} {val2:.1f} = {val1*val2:.1f}')
        
    case "/":
        
        if val2 == 0:
            print('Não existe divisão pro zero.')
            
        else:
            print(f'{val1:.1f} {op} {val2:.1f} = {val1/val2:.1f}')
        
    case _:
        print("Operador inválido.")
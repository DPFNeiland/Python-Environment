
placa = input()

if len(placa) == 8:
    if (placa[0].isalpha() and
        placa[1].isalpha() and
        placa[2].isalpha() and
        placa[3] == '-' and
        placa[4].isdigit() and
        placa[5].isdigit() and
        placa[6].isdigit() and
        placa[7].isdigit()):
        print(1)
    else:
        print(0)

elif len(placa) == 7:
    if (placa[0].isalpha() and
        placa[1].isalpha() and
        placa[2].isalpha() and
        placa[3].isdigit() and
        placa[4].isalpha() and
        placa[5].isdigit() and
        placa[6].isdigit()):
        print(2)
    else:
        print(0)

else:
    print(0)
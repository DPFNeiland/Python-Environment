


praca = input()

if (praca[3] == "S" and praca[4] == "P"):
    print("S")

elif  (praca[3] == "?" or praca[4] == "?") or  (praca[3] == "?" and praca[4] == "?") or (praca[3] == "?" and praca[4] == "P"):
    print("T")

else:
    print("N")
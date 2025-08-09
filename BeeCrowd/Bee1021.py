


B = float(input())

print("NOTAS:")
print(f"{B//100:.0f} nota(s) de R$ 100.00")
B = B - B//100*100

print(f"{B//50:.0f} nota(s) de R$ 50.00")
B = B - B//50*50

print(f"{B//20:.0f} nota(s) de R$ 20.00")
B = B - B//20*20

print(f"{B//10:.0f} nota(s) de R$ 10.00")
B = B - B//10*10

print(f"{B//5:.0f} nota(s) de R$ 5.00")
B = B - B//5*5

print(f"{B//2:.0f} nota(s) de R$ 2.00")
B = B - B//2*2

print("MOEDAS:")

print(f"{B//1:.0f} moeda(s) de R$ 1.00")
B = (B - B//1*1) * 100

print(f"{B//50:.0f} moeda(s) de R$ 0.50")
B = B - B//50*50

print(f"{B//25:.0f} moeda(s) de R$ 0.25")
B = B - B//25*25

print(f"{B//10:.0f} moeda(s) de R$ 0.10")
B = B - B//10*10

print(f"{B//5:.0f} moeda(s) de R$ 0.05")
B = B - B//5*5

print(f"{B//1:.0f} moeda(s) de R$ 0.01")
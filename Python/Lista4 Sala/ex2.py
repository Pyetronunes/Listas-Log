import math

a = []
for i in range(6):
    valor = int(input(f"Digite o {i+1} numero de A: "))
    a.append(valor)

b = []
for i in range(6):
    b.append(math.factorial(a[i]))

print(b)

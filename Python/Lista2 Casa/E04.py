n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

numeros = [n1, n2, n3]
numeros.sort()

print(f"Menor: {numeros[0]}")
print(f"Do meio: {numeros[1]}")
print(f"Maior: {numeros[2]}")

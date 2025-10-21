valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

if valor1>valor2:
    diferenca = valor1 - valor2
else:
    diferenca = valor2 - valor1

print(f"A diferença do valor maior para o menor é '%.2f'" %(diferenca))
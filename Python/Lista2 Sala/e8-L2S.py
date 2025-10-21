n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
n3 = int(input('Digite o terceiro numero:'))

print('\nNumeros divisiveis por 2 e 3:')

for n in[n1,n2,n3]:
    if n % 2 == 0 and n % 3 == 0:
        print(n)


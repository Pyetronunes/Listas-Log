num = int(input('Digite um numero inteiro: '))

if num > 0:
    print('O numero é POSITIVO.')
elif num <0:
    print('O numero é NEGATIVO.')
    print(f'O valor dele positivo é: {num*-1}')
else:
    print('O numero é ZERO.')

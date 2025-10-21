A = int(input('Digite o primeiro numero para formar o triangulo: '))
B = int(input('Digite o segundo numero para formar o triangulo: '))
C = int(input('Digite o terceiro numero para formar o triangulo: '))

if A+B > C and A+C > B and B+C > A:
    if A==B==C:
        print("Equilatero")
    elif A==B or A==C or B==C:
        print("Isosceles")
    else:
        print('Escaleno')
else:
    print('Os valores fornecidos nao formam um triangulo')
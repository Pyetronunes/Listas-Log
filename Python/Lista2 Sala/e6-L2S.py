import math

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if a==0:
    print('O valor de A deve ser diferente de zero.Isso NÃO é uma EQUAÇÃO DO SEGUNDO GRAU!')
else:
    delta = b**2-4*a*c

    if delta <0:
        print("Nao existe raizes reais.")
    elif delta>0:
        x = -b/(2*a)
    else:
        x1 = (-b +math.sqrt(delta))/(2*a)
        x2 = (-b -math.sqrt(delta))/(2*a)
        print("As duas raizes X1 e X2 sao: ", x1, x2)
    

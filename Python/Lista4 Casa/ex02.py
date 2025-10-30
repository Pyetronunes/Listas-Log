ra = input("Digite o RA: ")

if len(ra) != 9:
    print("O RA deve conter 9 digitos!")
else:
    PI= ra[:5]
    U = ra[5:]
    ra_novo = PI + U[::-1]
    print("RA novo:",ra_novo)
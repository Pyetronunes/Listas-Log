ra = input("Digite o RA: ")

if len(ra) != 9:
    print("O RA deve conter 9 digitos!")
else:
    primeiro = ra[:2][::-1]
    meio = ra[2:7]
    final = ra[7:][::-1]
    ra_novo = primeiro + meio + final
    print("Ra novo:", ra_novo)
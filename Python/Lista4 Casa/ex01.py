rav = input("Digite o RA alterado: ")

if len(rav) != 9:
    print("O RA deve conter 9 digitos!")
else:
    rac = {
        rav[0]+rav[1]+rav[7]+rav[6]+rav[4]+
        rav[5]+rav[2]+rav[3]+rav[8]
    }
print("RA corrigido:",rac)
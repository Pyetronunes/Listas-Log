nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2) / 2
if media >= 6.0:
    print(f"Parabens! Voce foi aprovado com média '%.2f'" %(media))
else:    
    nota_exame = float(input('Digite a nota do exame: '))
    nova_media = (media+nota_exame) / 2
    if nova_media >= 5.0:
        print(f"Parabens! Voce foi aprovado em exame com media '%.2f'" %(nova_media))
    else:
        print(f"Infelizmente voce nao foi aprovado com media '%.2f'" %(nova_media))
    
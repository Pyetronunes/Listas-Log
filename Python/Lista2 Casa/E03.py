import math

nota = float(input("Digite a nota: "))
resto = nota - int(nota)

if resto > 0.5:
    arredondada = math.ceil(nota)
else:
    arredondada = math.floor(nota)

print(f"Nota arredondada: {arredondada:.1f}")

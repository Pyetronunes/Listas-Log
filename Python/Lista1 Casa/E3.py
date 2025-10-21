import math

ap = float(input("Altura da parede (m): "))
lp = float(input("Largura da parede (m): "))
aa = float(input("Altura do azulejo (m): "))
la = float(input("Largura do azulejo (m): "))

qtd = (ap * lp) / (aa * la)
print(f"Quantidade de azulejos necessária: {math.ceil(qtd)}")

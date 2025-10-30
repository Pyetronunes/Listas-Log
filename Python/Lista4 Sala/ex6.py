A = []
for i in range(8):
    valor = int(input(f"Digite o {i+1} elemento de A: "))
    A.append(valor)

B = []
for i in range(8):
    B.append(A[i]**2)

print(B)
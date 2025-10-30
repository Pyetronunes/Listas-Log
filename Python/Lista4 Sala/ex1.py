A = []
for i in range(5):
    valor = int(input(f"Digite o {i+1} elemento de A: "))
    A.append(valor)

B = []
for i in range(5):
    B.append(A[i]*3)

print("Vetor B:", B)
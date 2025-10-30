A = []
for i in range(10):
    A.append(int(input(f"A[{i+1}]: ")))

B = list(reversed(A))

print("Vetor A:",A)
print("Vetor B:",B)
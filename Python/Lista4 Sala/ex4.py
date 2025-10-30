A = []
B = []

for i in range(5):
    A.append(int(input(f"A[{i+1}]: ")))
for i in range(5):
    B.append(int(input(f"B[{i+1}]: ")))

C = A+B

print(C)
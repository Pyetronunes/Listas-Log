import math

R = float(input("Digite o raio da esfera: "))

volume = (4/3) * math.pi * R**3
area = 4 * math.pi * R**2

print(f"Volume = {volume:.2f}, Área = {area:.2f}")

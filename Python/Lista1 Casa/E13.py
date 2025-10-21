s0 = 2
v0 = 3
a = 10

t = float(input("Digite o tempo (s): "))

s = s0 + v0*t + 0.5*a*(t**2)
print(f"Posição final s = {s:.2f} m")

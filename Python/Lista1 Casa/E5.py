massa = float(input("Digite sua massa (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = massa / (altura ** 2)
print(f"IMC = {imc:.2f}")

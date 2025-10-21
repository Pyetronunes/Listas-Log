total_salarios = 0

while True:
    salario_bruto = float(input("\nSalário bruto (0 para sair): "))
    if salario_bruto == 0:
        break

    horas = float(input("Horas trabalhadas no mês: "))

    if salario_bruto < 800:
        desconto = 0
    elif salario_bruto <= 1600:
        desconto = salario_bruto * (0.08 + 0.05)
    else:
        desconto = salario_bruto * (0.15 + 0.07)

    adicional = 0
    if horas > 160:
        valor_hora = salario_bruto / 160
        horas_extras = horas - 160
        adicional = horas_extras * valor_hora * 0.5

    salario_liquido = salario_bruto - desconto + adicional

    print(f"Salário líquido: R$ {salario_liquido:.2f}")
    total_salarios += salario_liquido

print(f"\nTotal geral dos salários líquidos: R$ {total_salarios:.2f}")

codigo = int(input("Digite o código do curso (1 a 5): "))

cursos = {
    1: "Engenharia",
    2: "Edificações",
    3: "Sistemas Elétricos",
    4: "Turismo",
    5: "Análise de Sistemas"
}

print(cursos.get(codigo, "Código inválido!"))

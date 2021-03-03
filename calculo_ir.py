#Calculo RI

salario = float(input("Insira o salario: "))

if salario <= 1903.98:
    print("Isento")
elif 1903.99 <= salario <= 2826.65:
    aliquota = 0.075
    deduzir = salario*aliquota
    print(f"Parcela a deduzir: {deduzir}")
elif 2826.66 <= salario <= 3751.05:
    aliquota = 0.15
    deduzir = salario * aliquota
    print(f"Parcela a deduzir: {deduzir}")
elif 3751.06 <= salario <= 4664.68:
    aliquota = 0.225
    deduzir = salario * aliquota
    print(f"Parcela a deduzir: {deduzir}")
elif salario > 4664.68:
    aliquota = 0.275
    deduzir = salario * aliquota
    print(f"Parcela a deduzir {deduzir}")
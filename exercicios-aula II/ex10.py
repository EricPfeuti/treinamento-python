# Exercício 10 - Salário no Mês

valorPorHora = float(input("Digite aqui quanto você ganha por hora (R$): "))
horasTrabalhadas = float(input("Digite aqui o número de horas trabalhadas no mês: "))

salario = valorPorHora * horasTrabalhadas

print(f"O seu salário é de R${salario:.2f}")
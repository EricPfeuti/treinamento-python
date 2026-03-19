# Exercício 2 - Turno de Trabalho
turnoTrabalho = input("Digite aqui o turno de trabalho (N ou D): ")
horas = float(input("Digite aqui quantidade de horas trabalhadas: "))

if turnoTrabalho == "N":
    valorHora = 45
else:
    valorHora = 37.5

salario = horas * valorHora

print(f"O salário do funcionário é de ${salario:.2f}")

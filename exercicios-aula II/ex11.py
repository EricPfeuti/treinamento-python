# Exercício 11 - Cálculo IMC

peso = float(input("Digite aqui seu peso (kg): "))
altura = float(input("Digite aqui sua altura (m): "))

imc = peso / (altura * altura)

print(f"Seu Índice de Massa Corporal é de {imc:.2f}")
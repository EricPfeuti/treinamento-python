# Exercício 8 - Calcular e Imprimir Gastos de Um Paciente

print("Gastos Paciente")
print("Tipos de Quarto:\n-Particular (1)\n-Semi-particular (2)\n-Coletivo (3)")
print()

numeroDias = int(input("Digite aqui o número de dias gastos no hospital: "))
tipoQuarto = int(input("Digite aqui o tipo do seu quarto (1, 2 ou 3): "))
wifi = int(input("Você utilizou Wi-Fi sim (1) ou não (2)? "))
tv = int(input("Você utilizou TV a cabo sim (1) ou não (2)? "))

if tipoQuarto == 1:
    valorQuarto = 360
elif tipoQuarto == 2:
    valorQuarto = 210
elif tipoQuarto == 3:
    valorQuarto = 185
else:
    print("Lembre-se de que o quarto particular = 1, semi = 2 e coletivo = 3")

if wifi == 1:
    valorWifi = 3

if tv == 1:
    valorTv = 4

valorTotal = valorQuarto * numeroDias + valorWifi + valorTv

print(f"Número de dias no hospital: {numeroDias}\nDiárias: R${valorQuarto * numeroDias}\nWifi: R${valorWifi}\nTV: R${valorTv}\nTotal: R${valorTotal}")
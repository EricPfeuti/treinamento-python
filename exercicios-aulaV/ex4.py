# Exercício 4 - Contas
contaAgua = float(input("Digite aqui o valor da conta de água (R$): "))
contaLuz = float(input("Digite aqui o valor da conta de luz (R$): "))
contaTelefone = float(input("Digite aqui o valor da conta de telefone (R$): "))
salario = float(input("Digite aqui o valor do salário (R$): "))
contas = contaAgua + contaLuz + contaTelefone

if contas < salario:
    salarioRestante = salario - contas
else:
    print("Salário Insuficiente!")

print(f"Ao pagar as contas com o salário de R${salario:.2f} sobrará R${salarioRestante:.2f}")
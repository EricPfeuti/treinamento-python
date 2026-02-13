# Exercício 4 - Valor Prestação em Atraso
valorPrestacao = float(input("Digite o valor da prestação (R$): "))
multa = int(input("Digite a porcentagem de multa pelo atraso (%): "))
qtdeDias = int(input("Digite a quantidade de dias de atraso: "))

prestacao = valorPrestacao + (valorPrestacao * (multa/100) * qtdeDias)

print(f"O valor da prestação atualizado é de R${prestacao:.2f}.")
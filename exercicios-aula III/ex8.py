# Exercício 8 - Taxa
valorTotalConta = float(input("Digite aqui o valor total da conta (R$): "))
taxaServico = float(input("Digite aqui a taxa de serviço (%): "))
numeroPessoas = int(input("Digite aqui o número de pessoas no grupo: "))

valorTaxa = valorTotalConta * (taxaServico / 100)
valorTotal = valorTotalConta + valorTaxa
valorPessoa = valorTotal / numeroPessoas

print(f"A taxa de serviço é de R${valorTaxa:.2f} \nO valor total com taxa é de R${valorTotal:.2f} \nO valor por pessoa é de R${valorPessoa:.2f}")
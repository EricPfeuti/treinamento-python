# Exercício 3 - Desconto
valorCompra = float(input("Digite aqui o valor da compra (R$): "))

if valorCompra > 200:
    desc = 0.8
else:
    desc = 1

valorFinal = valorCompra * desc

print(f"Aplicando o desconto sua compra ficou igual R${valorFinal:.2f}")
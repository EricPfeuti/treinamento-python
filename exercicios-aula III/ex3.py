valorOriginal = float(input("Digite o valor original da compra: "))
valorDesconto = valorOriginal * 0.12
valorFinal = valorOriginal - valorDesconto

print(f"Valor Original: R${valorOriginal:.2f} | Desconto: R${valorDesconto:.2f} | Valor a Pagar: R${valorFinal:.2f}")
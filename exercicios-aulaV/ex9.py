# Exercício 9 - Mostar Preço da Etiqueta de Produto

print("1- À vista em dinheiro ou cheque, recebe 10% de desconto \n2- À vista no cartão de crédito, recebe 5% de desconto \n3- Em 2 vezes, preço normal de etiqueta sem juros \n4- Em 3 vezes, preço normal de etiqueta mais juros de 10%")

precoProduto = float(input("Digite aqui o preço do produto (R$): "))
formaPagamento = int(input("Digite aqui a forma de pagamento (1 a 4):"))

if formaPagamento == 1:
    precoFinal = precoProduto * 0.9
elif formaPagamento == 2:
    precoFinal = precoProduto * 0.85
elif formaPagamento == 3:
    precoFinal = precoProduto
elif formaPagamento == 4:
    precoFinal = precoProduto * 1.1
else:
    print("Selecione forma de pagamento.")

print(f"Valor a pagar: R$ {precoFinal:.2f}")
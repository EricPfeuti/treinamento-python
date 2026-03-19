# Exercício 7 - Comércio
nomeProduto = str(input("Digite aqui o nome do produto: "))
valor = float(input("Digite aqui o valor da compra (R$): "))

if valor < 10:
    lucro = 0.7
elif 10 <= valor < 30:
    lucro = 0.5
elif 30 <= valor < 50:
    lucro = 0.4
else:
    lucro = 0.3

valorVenda = valor * (1 + + lucro)
print(f"Com a venda do produto {nomeProduto} o comerciante terá um lucro de R${valorVenda}")
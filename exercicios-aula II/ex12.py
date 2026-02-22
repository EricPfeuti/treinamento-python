# Exercício 12 - Aluguel Carro

qntdKmPercorridos = float(input("Digite aqui a quantidade de km percorridos: "))
qntdDias = int(input("Digite aqui a quantidade de dias pelos quais o carro foi alugado: "))

preco = (qntdDias * 60) + (qntdKmPercorridos * 0.15)

print(f"O preço a pagar do aluguel deste carro será de R${preco:.2f}")
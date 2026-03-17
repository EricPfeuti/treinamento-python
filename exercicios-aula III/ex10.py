# Exercício 10 - Área e Litros de Tinta

altura = float(input("Digite aqui a altura da parede (m): "))
largura = float(input("Digite aqui a largura da parede (m): "))
rendimentoTinta = float(input("Digite aqui quantos metros quadrados um Litro cobre: "))

areaTotal = altura * largura
litrosNecessarios = areaTotal / rendimentoTinta

print(f"A área total é de {areaTotal:.2f} metros quadrados \nSerão necessários {litrosNecessarios:.2f} litros de tinta")

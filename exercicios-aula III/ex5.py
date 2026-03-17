# Exercício 5 - Qntd Total de Litros e Custo Combustível

distanciaTotal = float(input("Digite aqui a distância total da viagem (Km): "))
kmPorLitro = float(input("Digite aqui o consumo médio em Km por litro (Km/L): "))
valorLitro = float(input("Digite aqui o valor do litro do combustível (R$): "))

litrosNecessarios = distanciaTotal / kmPorLitro
custoTotal = litrosNecessarios * valorLitro

print(f"Quantidade total de litros necessários para viagem = {litrosNecessarios:.2f} \nCusto total de combustível = R${custoTotal: .2f} ")
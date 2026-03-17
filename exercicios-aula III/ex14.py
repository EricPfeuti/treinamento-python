# Exercício 14 - Lado e Área Total do terreno

a = float(input("Digite a largura da casa: "))
b = float(input("Digite o comprimento da casa: "))
c = float(input("Digite a % de construção casa: "))

area = a * b
areaTotal = (area * 100) / c
lado = int(areaTotal ** 0.5)

print(f"Total que pode ser construído {areaTotal:.2f} metros quadrados")
print(f"O lado do terreno deve ser {lado} metros")
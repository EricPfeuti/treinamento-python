# Exercício 12 - Fábrica
qntdPecas = int(input("Digite aqui a quantidade de peças produzidas por hora: "))
horas = float(input("Digite aqui o número de horas trabalhadas: "))
percentualPecasDescartadas = float(input("Digite aqui porcentagem de peças descartadas (%): "))

totalProduzido = qntdPecas * horas
totalDescartado = totalProduzido * (percentualPecasDescartadas/100)
pecasAproveitadas = totalProduzido - totalDescartado

print(f"O total de peças produzidas é de {totalProduzido}. Já o total descartado é de {totalDescartado} peças, sendo aproveitadas {pecasAproveitadas} peças")
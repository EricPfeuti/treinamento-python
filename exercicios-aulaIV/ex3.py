# Exercício 3 - Média Ponderada

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

p1 = float(input("Digite aqui o peso da nota 1: "))
p2 = float(input("Digite aqui o peso da nota 2: "))
p3 = float(input("Digite aqui o peso da nota 3: "))
p4 = float(input("Digite aqui o peso da nota 4: "))

media = (n1*p1 + n2*p2 + n3*p3 + n4*p4) / (p1 + p2 + p3 + p4)
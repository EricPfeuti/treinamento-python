# Exercício 14 - Menor quantidade de notas
produto = int(input("Entre com o preço do produto (R$): "))

n100 = produto // 100 # quociente
produto = produto % 100 # resto

n50 = produto // 50
produto = produto % 50

n20 = produto // 20
produto = produto % 20

n10 = produto // 10
produto = produto % 10

n5 = produto // 5
produto = produto % 5

n2 = produto // 2
produto = produto % 2

n1 = produto // 1
produto = produto % 1

print(f"Notas de 100: {n100} \n Notas de 50: {n50} \n Notas de 20: {n20} \n Notas de 10: {n10} \n Notas de 5: {n5} \n Notas de 2: {n2} \n Notas de 100: {n1}")
# Exercício 8 - Troca de Valores

n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite um segundo valor inteiro: "))

print(f"Antes:\n n1 = {n1}\n n2 = {n2}")

n1, n2 = n2, n1

print(f"Depois:\n n1 = {n1} \n n2 = {n2}")
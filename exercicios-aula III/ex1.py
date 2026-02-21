valorNota1 = float(input("Digite a nota 1: "))
valorNota2 = float(input("Digite a nota 2: "))
valorNota3 = float(input("Digite a nota 3: "))

mediaPonderada = ((valorNota1 * 2) + (valorNota2 * 3) + (valorNota3 * 5))/10

print(f"A média ponderada é igual a {mediaPonderada:.2f} pontos.")
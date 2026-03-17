# Exercício 2 - Capital de Juros

capital = float(input("Digite aqui o capital incial(R$): "))
juros = float(input("Digite aqui a taxa de juros(%): "))
tempo = float(input("Digite aqui o tempo de aplicação: "))

m = capital * (1 + (juros / 100)) ** tempo

print(f"Capital Inicial: {capital} ")
print(f"Tempo em meses: {tempo * 12}")
print(f"Taxa para decimal: {juros / 100}")
print(f"Montante final arredondado para 2 casas decimais: {m:.2f}")
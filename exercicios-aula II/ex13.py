# Exercício 13 - Aumento Salário

salario = float(input("Digite aqui seu salário (R$): "))
percentualAumento = float(input("Digite aqui o percentual de aumento (%): "))

novoSalario = (salario * (percentualAumento/100)) + salario

print(f"Seu salário era de R${salario}\nAgora seu salário com o percentual de aumento de {percentualAumento}% ficou de R${novoSalario:.2f}")
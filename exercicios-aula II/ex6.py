# Exercício 6 - Valor em Reais

cotacaoDolar = float(input("Digite a cotação do dólar: "))
dolar = float(input("Digite agora um valor em dólar: "))
valorReal = cotacaoDolar * dolar

print(f"O valor ${dolar:.2f} é igual a R${valorReal:.2f}.")
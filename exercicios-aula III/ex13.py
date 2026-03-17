# Exercício 13 - Custo Mensal de Equipamento
potencia = float(input("Digite aqui a potência do equipamento (W): "))
horas = float(input("Digite aqui o número de horas de uso diário: "))
dias = int(input("Digite aqui o número de dias de utilização: "))
kWh = float(input("Digite aqui o preço da energia por kWh: "))

consumoTotal = potencia * horas * dias
kWhConvertido = consumoTotal / 1000
custoTotal = kWh * kWhConvertido

print(f"O consumo total é de {consumoTotal:.2f} Wh. O valor convertido fica igual a {kWhConvertido} kWh e o custo total é de R${custoTotal}")
# Exercício 6 - Taxa Detran
anoCarro = int(input("Digite aqui o ano do carro: "))
precoCarro = float(input("Digite aqui o preço dele (R$): "))

if anoCarro < 2010:
    taxa = precoCarro * 0.025
else:
    taxa = precoCarro * 0.035

print(f"A taxa a ser pago do veículo do ano {anoCarro} será de R${taxa:.2f}")
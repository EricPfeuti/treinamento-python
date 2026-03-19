# Exercício 6 - Investidor II
valorTotalInvestido = float(input("Digite aqui o valor total investido (R$): "))
CDIanual = float(input("Digite aqui o valor do CDI anual (%): "))
percentualCDI = float(input("Digite aqui o percentual do CDI pago pela LCI (%): "))
dividendYieldFII = float(input("Digite aqui o Dividend Yield do FII (%): "))
valorizacaoAnualFII = float(input("Digite aqui a valorização anual do FII (%): "))
tempo = int(input("Digite aqui o tempo em anos: "))

valorDividido = valorTotalInvestido / 2

taxaLCI = (CDIanual * percentualCDI / 100) / 100
montanteLCI = valorDividido * (1 +  taxaLCI) ** tempo

taxaFII = valorizacaoAnualFII / 100
valorizacaoCompostaFII = valorDividido * (1 + taxaFII) ** tempo

dividendos = valorDividido * (dividendYieldFII / 100) * tempo
montanteTotalFII = valorizacaoCompostaFII + dividendos

valorTotal = montanteLCI + montanteTotalFII
percentualRetorno = (valorTotal - valorTotalInvestido) / valorTotalInvestido * 100

diferenca = montanteTotalFII - montanteLCI
raizCubica = valorTotal ** (1/3)

print(f"Montante de cada ativo: LCI R${montanteLCI:.2f} e FII R${montanteTotalFII:.2f} \nTotal de carteira: R${valorTotal:.2f} \nDiferença absoluta entre FII e LCI: R${diferenca:.2f} \nRaíz cúbica do total: R${raizCubica:.2f}")
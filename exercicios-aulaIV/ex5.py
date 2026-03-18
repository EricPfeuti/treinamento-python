# Exercício 5 - Investidor
import math

valorInvestido = float(input("Digite aqui o valor investido (R$): "))
CDIanual = float(input("Digite aqui o CDI anual (%): "))
tempoAnos = int(input("Digite aqui o tempo em anos: "))

meses = tempoAnos * 12

CDImensal = (CDIanual / 12) / 100

taxaMensalCDB = CDImensal * 1.10
taxaMensalLCI = CDImensal * 0.95

montanteFinalPoupanca = valorInvestido * (1 + 0.005) ** meses
montanteFinalCDB = valorInvestido * (1 + taxaMensalCDB) ** meses

lucroCDB = montanteFinalCDB - valorInvestido
IRregressivo = lucroCDB * 0.15
montanteLiquidoCDB = montanteFinalCDB - IRregressivo

montanteFinalLCI = valorInvestido * (1 + taxaMensalLCI) ** meses

melhor = montanteFinalPoupanca

if montanteLiquidoCDB > melhor:
    melhor = montanteLiquidoCDB
if montanteFinalLCI > melhor:
    melhor = montanteFinalLCI

pior = montanteFinalPoupanca

if montanteLiquidoCDB < pior:
    pior = montanteLiquidoCDB
if montanteFinalLCI < pior:
    pior = montanteFinalLCI

diferenca = melhor - pior
percentualVantagem = (diferenca / pior) * 100
raizDiferenca = math.sqrt(diferenca)

print(f"Poupança: R${montanteFinalPoupanca:.2f} \nCDB Líquido: R${montanteLiquidoCDB:.2f} \nLCI: R${montanteFinalLCI:.2f} \nDiferença entre melhor e pior: R${diferenca:.2f} \nVantagem (%): {percentualVantagem:.2f}% \nRaíz quadrada da diferença: {raizDiferenca:.2f}")
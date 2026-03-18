# Exercício 4 - Epidemia
import math

qntdInicial = int(input("Digite aqui a quantidade inicial de pessoas infectadas: "))
janelaTemporal = float(input("Digite aqui o número total de períodos de tempo que serão analisados: "))

cargaViral = qntdInicial * (2 ** janelaTemporal)
contagioAcumulado = qntdInicial * (2 ** (janelaTemporal + 1) - 1) / (2 -1)
deltaExpansao = cargaViral - qntdInicial
escalaLogaritma = math.log(cargaViral)

print(f"A carga viral é de {cargaViral:.4f} infectados \nO contágio acumulado é de {contagioAcumulado:.4f} infectados \nDelta de expansão é de {deltaExpansao:.4f} infectados \nJá a escala logarítmica é de {escalaLogaritma:.4f}")
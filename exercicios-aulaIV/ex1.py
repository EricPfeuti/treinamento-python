# Exercício 1 - Ingressos
import math

custoEspetaculo = float(input("Digite aqui o total do espetáculo (R$): "))
precoIngresso = float(input("Digite aqui o preço do ingresso (R$): "))

qntd = custoEspetaculo / precoIngresso

qntdLucro = qntd * 1.23

print(f"Mínimo de ingressos: {math.ceil(qntd)}")
print(f"Ingressos para ter lucro de 23%: {math.ceil(qntdLucro)}")
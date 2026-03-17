# Exercicio 6 - Altura (m, cm e mm)
altura = float(input("Digite aqui a sua altura (m): "))

alturaCm = altura * 100
alturaMm = alturaCm * 10

print(f"Sua altura é de {altura:.2f} metros, {alturaCm:.2f} centímetros e de {alturaMm:.2f} milímetros.")
# Exercício 1 - Volume do Tronco de uma Pirâmide

h = 0.0
baseMaior = 0.0
baseMenor = 0.0
volume = 0.0

h = float(input("Digite a altura do tronco: "))
baseMaior = float(input("Digite a base maior: "))
baseMenor = float(input("Digite a base menor: "))

volume = h/3 * (baseMaior**2 + baseMenor**2 + (baseMaior**2 * baseMenor**2)**0.5)
print(f"Volume = {volume:.2f}")
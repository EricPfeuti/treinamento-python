valorSegundos = int(input("Digite um valor em segundos: "))

valorHora = valorSegundos // 3600
resto = valorSegundos % 3600
valorMinutos = resto // 60
valorSegundosRestantes = resto % 60

print(f"{valorHora:02d}:{valorMinutos:02d}:{valorSegundosRestantes:02d}")
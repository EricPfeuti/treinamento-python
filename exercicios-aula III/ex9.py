# Exercício 9 - Conversão de Valor em Kbps para Mbps e bps

valorKbps = float(input("Digite aqui um valor (Kbps): "))

valorMbps = valorKbps / 1000
valorbps = valorKbps * 1000

print(f"{valorKbps} Kbps = {valorMbps:.2f} Mbps = {valorbps:.2f} bps")
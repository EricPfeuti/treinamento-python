valorReal = float(input("Digite o valor real representando uma quantia em GB: "))
valorMegabyte = valorReal * 1024
valorKylobyte = valorMegabyte * 1024

print(f"GB: {valorReal:.2f}\n MB: {valorMegabyte:.2f}\n KB: {valorKylobyte:.2f}")
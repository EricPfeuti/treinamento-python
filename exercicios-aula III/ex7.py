# Exercício 7 - Capacidade Total de um disco em TB
capacidadeDisco = float(input("Digite a capacidade de um disco (GB): "))
qntdDiscos = float(input("Digite a quantidade de discos instalados: "))

capacidadeTotal = capacidadeDisco * qntdDiscos
valorTotal = capacidadeTotal / 1024

print(f"O valor total convertido para TeraBytes (TB) é de {valorTotal:.2f} TB.")
# Exercício 11 - Frete por Região
nome_cliente = input("Digite o nome do cliente: ")
nome_vendedor = input("Digite o nome do vendedor: ")
regiao = int(input("Digite o código da região (1-Sul, 2-Norte, 3-Leste, 4-Oeste): "))
num_pecas = int(input("Digite o número de peças vendidas: "))

frete_unitario = 0

if regiao == 1:
    frete_unitario = 1.00 if num_pecas <= 1000 else 0.90
elif regiao == 2:
    frete_unitario = 1.10 if num_pecas <= 1000 else 1.00
elif regiao == 3:
    frete_unitario = 1.15 if num_pecas <= 1000 else 1.10
elif regiao == 4:
    frete_unitario = 1.20 if num_pecas <= 1000 else 1.15
else:
    print("Código de região inválido!")
    exit()

custo_total = num_pecas * 7
valor_total_venda = custo_total * 1.5
valor_frete = num_pecas * frete_unitario
comissao_vendedor = valor_total_venda * 0.065
lucro_obtido = valor_total_venda - custo_total - comissao_vendedor

print("-" * 30)
print(f"Relatório de Venda - Vendedor: {nome_vendedor}")
print(f"Cliente: {nome_cliente}")
print("-" * 30)
print(f"Valor do Frete: R$ {valor_frete:.2f}")
print(f"Comissão do Vendedor: R$ {comissao_vendedor:.2f}")
print(f"Lucro Obtido: R$ {lucro_obtido:.2f}")
print("-" * 30)
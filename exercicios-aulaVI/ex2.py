# Exercício 2 - Valor da Parcela

def calcular_parcela(valor_compra, qntd_parcelas):
    valor_juros = valor_compra * 1.05
    
    valor_parcela = valor_juros / qntd_parcelas
    
    return valor_parcela
    
def main():
    valor_compra = float(input("Digite aqui o valor da compra (R$): "))
    qntd_parcelas = int(input("Digite aqui a quantidade de parcelas: "))
    
    valor_parcela = calcular_parcela(valor_compra, qntd_parcelas)
    
    print(f"O valor da parcela com 5% de juros é de R${valor_parcela}")

main()
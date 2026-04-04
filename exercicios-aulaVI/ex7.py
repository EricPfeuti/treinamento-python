# Exercício 7 - Valor Final Compra, Descontos, Imposto
def calcular_total(produto, quantidade):
    total = produto * quantidade
    return total

def aplicar_desconto(total):
    if total >= 500:
        total_com_desconto = total * 0.88 
    elif total >= 200:
        total_com_desconto = total * 0.93
    elif total >= 100:
        total_com_desconto = total * 0.95 
    else:
        total_com_desconto = total 
    return total_com_desconto

def calcular_imposto(valor):
    valor_final = valor * 1.08
    return valor_final

def main():
    preco = float(input("Digite o preço do produto (R$): "))
    qntd_comprada = int(input("Digite a quantidade comprada: "))

    bruto = calcular_total(preco, qntd_comprada)
    com_desconto = aplicar_desconto(bruto)
    valor_final = calcular_imposto(com_desconto)

    print(f"Valor Bruto: R$ {bruto:.2f}")
    print(f"Valor com Desconto: R$ {com_desconto:.2f}")
    print(f"Valor Final (com imposto de 8%): R$ {valor_final:.2f}")

main()
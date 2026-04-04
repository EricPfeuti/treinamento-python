# Exercício 5 - Salário
def calcular_salario(salario_base, vendas):
    bonus = vendas*0.07
    salario_final = salario_base + bonus
    
    print(f"Salário final de R${salario_final:.2f}")

def main():
    salario_base = float(input("Digite aqui o valor do salário base (R$): "))
    vendas = int(input("Digite quantas vendas foram realizadas: "))

    calcular_salario(salario_base, vendas)
    
main()
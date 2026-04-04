# Exercício 1 - Distância, Consumo Médio e Valor Gasto
def converter_valores(km_inicial, km_final, litros_gastos, preco_litro):
    distancia = km_final - km_inicial
    consumo_medio = distancia / litros_gastos
    valor_total = litros_gastos * preco_litro
    
    print(f"Distância: {distancia:.2f}km")
    print(f"Consumo Médio: {consumo_medio:.2f} km/L")
    print(f"Valor Total: R${valor_total:.2f}")
    
def main():
    quilometragem_inicial = float(input("Digite aqui a quilometragem inicial (km): "))
    quilometragem_final = float(input("Digite aqui a quilometragem final (km): "))
    litros_gastos = float(input("Digite aqui a quanitdade de litros gastos: "))
    preco_litro = float(input("Digite aqui o preço do litro (R$): "))
    
    converter_valores(quilometragem_inicial, quilometragem_final, litros_gastos, preco_litro)

main()
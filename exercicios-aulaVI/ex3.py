# Exercício 3 - Calcular Velocidade
def calcular_velocidade(distancia, tempo):
    return distancia / tempo

def main():
    distancia_obj1 = float(input("Digite aqui a distância percorrida pelo objeto 1 (Km):"))
    tempo_obj1 = float(input("Digite aqui o tempo (h):"))
    print()
    distancia_obj2 = float(input("Digite aqui a distância percorrida pelo objeto 2 (Km):"))
    tempo_obj2 = float(input("Digite aqui o tempo (h):"))
    print()
    distancia_obj3 = float(input("Digite aqui a distância percorrida pelo objeto 3 (Km):"))
    tempo_obj3 = float(input("Digite aqui o tempo (h):"))
    
    velocidade_obj1 = calcular_velocidade(distancia_obj1, tempo_obj1)
    velocidade_obj2 = calcular_velocidade(distancia_obj2, tempo_obj2)
    velocidade_obj3 = calcular_velocidade(distancia_obj3, tempo_obj3)
    
    print(f"A velocidade do Objeto 1 é de {velocidade_obj1:.2f}Km/h")
    print(f"A velocidade do Objeto 2 é de {velocidade_obj2:.2f}Km/h")
    print(f"A velocidade do Objeto 3 é de {velocidade_obj3:.2f}Km/h")

main()
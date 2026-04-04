# Exercício 6 - Calcular Média
def calcular_media(pontualidade, produtividade, quantidade):
    media_final = (pontualidade + produtividade + quantidade) / 3
    return media_final
    
def classificar_desempenho(media_final):
    if media_final >= 8:
        return "Excelente"
    elif media_final >= 6:
        return "Bom"
    elif media_final >= 4:
        return "Regular"
    else:
        return "Insatisfatório"
    
def main():
    n1 = float(input("Digite aqui a nota de pontualidade: "))
    n2 = float(input("Digite aqui a nota de produtividade: "))
    n3 = float(input("Digite aqui a nota da prova:"))
    
    media_final = calcular_media(n1, n2, n3)
    desempenho = classificar_desempenho(media_final)
    
    print(f"Média Final: {media_final:.2f}")
    print(f"Classificação: {desempenho}")
    
main()
def exibir_mensagem():
    print("O programa funciona com a escolha de uma opção de converter Fahrenheit para Celsius (F) ou converter Celsius para Fahrenheit (C). Para a primeira opção digite (F) e a segunda digite (C)")

def escolher_opcao():
    print("F: Converter Fahrenheit para Celsius")
    print("C: Converter Celsius para Fahrenheit")
    
    opcao = input("Digite a sua opção (F ou C): ")
    return opcao

def ler_temperatura():
    temp = int(input("Digite o valor inteiro da temperatura: "))
    return temp

def fahrenheit_para_celsius(tempF):
    celsius = (tempF - 32) / 1.8
    return celsius

def celsius_para_fahrenheit(tempC):
    fahrenheit = (tempC * 1.8) + 32
    return fahrenheit

def main():
    exibir_mensagem()
    
    opcao = escolher_opcao()
    
    if opcao == 'F':
        valor = ler_temperatura()
        resultado = fahrenheit_para_celsius(valor)
        print(f"{valor}°F equivale a {resultado:.2f} °C")
        
    elif opcao == 'C':
        valor = ler_temperatura()
        resultado = fahrenheit_para_celsius(valor)
        print(f"{valor}°C equivale a {resultado:.2f} °F")
        
    else:
        print("Opção inválida!")

main()
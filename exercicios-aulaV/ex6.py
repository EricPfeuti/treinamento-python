# Exercício 7 - Número Divisivel por 3 e5
numero = float(input("Digite aqui o número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"O número {numero} é divisível por 3 e 5 ao mesmo tempo!")
else:
    print(f"O número {numero} não é divisível por 3 e 5 ao mesmo tempo!")
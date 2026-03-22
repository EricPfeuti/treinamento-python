# Exercício 10 - Crime
a = int(input("Telefonou para a vítima? (Sim = 1 ou Não = 0) "))
b = int(input("Esteve no local do crime? (Sim = 1 ou Não = 0) "))
c = int(input("Mora perto da vítima? (Sim = 1 ou Não = 0) "))
d = int(input("Devia para a vítima? (Sim = 1 ou Não = 0) "))
e = int(input("Já trabalhou com a vítima? (Sim = 1 ou Não = 0) "))

if a + b + c + d + e == 2:
    print("Classifacação: Suspeita")
elif 3 <= a + b + c + d + e <= 4:
    print("Classifacação: Cúmplice")
elif a + b + c + d + e == 5:
    print("Classifacação: Assassino")
else:
    print("Classifacação: Inocente")



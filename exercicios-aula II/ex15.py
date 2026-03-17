# Exercício 15 - Tempo para arquivo ser visualizado

x = float(input("Digite a velocidade do modem (Kbps): "))
y = float(input("Velocidade do disco rígido de memória (Bps): "))
z = float(input("Tamanho do arquivo (MB): "))

arquivoParaBits = z * 8000000
arquivoParaBytes = z * 1000000

tempo1 = arquivoParaBits / (x * 1000)
tempo2 = arquivoParaBytes / y
tempoTotal = tempo1 + tempo2

print(f"Tempo total é de {tempoTotal} segundos.")
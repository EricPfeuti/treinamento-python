# Exercício 11 - Tempo Gasto na Transferência
arquivo = float(input("Ditei aqui o tamanho do arquivo (MB): "))
tempoTotal = float(input("Digite aqui o tempo total de download (s): "))

velocidadeMedia_mbs = arquivo / tempoTotal
velocidadeMedia_Mbps = velocidadeMedia_mbs * 8

print(f"A velocidade média de transferência é de {velocidadeMedia_mbs:.3f} MB/s e de {velocidadeMedia_Mbps:.3f} Mbps")
from datetime import datetime, timedelta
import hashlib
import os

# Exercício 1
def avaliar_temperatura(temp: float) -> str:
    if (temp <= 20):
        return "Frio"
    elif(20 <= temp < 40):
        return "Ideal"
    elif(40 <= temp < 70):
        return "Alerta"
    else:
        return "Risco crítico"
    
# Exercício 2
def avaliar_cpu(uso: float) -> str:
    if (uso < 40):
        return "Normal"
    elif(40 <= uso < 80):
        return "Alta"
    else:
        return "Sobrecarga"
    
# Exercício 3
def avaliar_memoria(mem: float) -> str:
    if (mem < 50):
        return "Confortável"
    elif(50 <= mem < 85):
        return "Monitorar"
    else:
        return "Crítica"

# Exercício 4
def classificar_latencia(lat: float) -> str:
    if (lat < 10):
        return "Excelente"
    elif(10 >= lat < 40):
        return "Boa"
    elif(40 <= lat < 100):
        return "Regular"
    else:
        return "Ruim"
    
# Exercício 5
def avaliar_disco(espaco_livre: float) -> str:
    if(espaco_livre < 20):
        return "Crítico"
    if(20 >= espaco_livre < 40):
        return "Atenção"
    else:
        return "Seguro"
    
# Exercício 6
def validar_certificado(data_emissao: str, anos: int) -> str:
    data = datetime.strptime(data_emissao, "%d/%m/%Y")
    data_expiracao = data + timedelta(days=anos * 365)
    hoje = datetime.now()

    if hoje > data_expiracao:
        return "Certificado expirado"
    elif (data_expiracao - hoje).days <= 30:
        return "Certificado expira em breve"
    else:
        return "Certificado válido"
    
# Exercício 7
def prever_armazenamento(inicial: float, taxa: float, anos: int) -> tuple:
    final = inicial * (1 + taxa) ** anos

    if final < 500:
        status = "Seguro"
    elif final < 2000:
        status = "Monitorar"
    else:
        status = "Upgrade necessário"

    return final, status

# 🔥 Exercício 8
def analisar_trafego(r1: float, r2: float, r3: float) -> tuple:
    media = (r1 + r2 + r3) / 3

    if media < 100:
        status = "Baixo tráfego"
    elif 100 <= media < 500:
        status = "Tráfego moderado"
    else:
        status = "Tráfego alto"

    return media, status

# Exercício 9
def gerar_id_evento(nome_servidor: str, timestamp: str) -> str:
    texto = nome_servidor + timestamp
    return hashlib.sha256(texto.encode()).hexdigest()

# 🔥 Exercício 10
def identificar_so() -> str:
    so = os.name

    if so == "nt":
        return "Windows"
    elif so == "posix":
        return "Linux/Unix"
    else:
        return "Outro sistema"

# Exercício 11
def avaliar_datacenter(temp, cpu, mem, lat, disco) -> str:
    if temp > 70 or cpu > 90 or mem > 90 or disco < 10:
        return "Servidor crítico"
    elif lat > 100 or temp > 40:
        return "Servidor em alerta"
    else:
        return "Servidor estável"
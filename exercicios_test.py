from exercicios import avaliar_temperatura, avaliar_cpu, avaliar_memoria, classificar_latencia, avaliar_disco, validar_certificado, prever_armazenamento, analisar_trafego, gerar_id_evento, identificar_so, avaliar_datacenter

def test_avaliar_temperatura():
    assert avaliar_temperatura(10), "Frio"
    assert avaliar_temperatura(21), "Ideal"
    assert avaliar_temperatura(41), "Alerta"
    assert avaliar_temperatura(71), "Risco crítico"
    
def test_avaliar_cpu():
    assert avaliar_cpu(21), "Normal"
    assert avaliar_cpu(41), "Alta"
    assert avaliar_cpu(71), "Sobrecarga"

def test_avaliar_memoria():
    assert avaliar_memoria(49), "Normal"
    assert avaliar_memoria(51), "Alta"
    assert avaliar_memoria(86), "Sobrecarga"

def test_classificar_latencia():
    assert classificar_latencia(9), "Excelente"
    assert classificar_latencia(19), "Boa"
    assert classificar_latencia(51), "Regular"
    assert classificar_latencia(106), "Ruim"

def test_avaliar_disco():
    assert avaliar_disco(19), "Crítico"
    assert avaliar_disco(39), "Atenção"
    assert avaliar_disco(51), "Seguro"
    
def test_validar_certificado():
    assert validar_certificado("01/01/2000", 1), "Certificado expirado"
    assert validar_certificado("01/01/2025", 10), "Certificado válido"

    from datetime import datetime, timedelta
    
    hoje = datetime.now()
    data_emissao = (hoje - timedelta(days=335)).strftime("%d/%m/%Y")
    
    assert validar_certificado(data_emissao, 1) == "Certificado expira em breve"
    
def test_prever_armazenamento():
    assert prever_armazenamento(100, 0.1, 2), "Seguro"
    assert prever_armazenamento(500, 0.5, 2), "Monitorar"
    assert prever_armazenamento(1000, 0.5, 2), "Updgrade Necessário"

def test_analisar_trafego():
    assert analisar_trafego(50, 60, 70), "Baixo tráfego"

def test_gerar_id_evento():
    id1 = gerar_id_evento("server1", "123")
    id2 = gerar_id_evento("server1", "123")
    
    assert id1 == id2
    assert len(id1) == 64

def test_identificar_so():
    assert identificar_so() in ["Windows", "Linux/Unix", "Outro sistema"]

def test_avaliar_datacenter():
    assert avaliar_datacenter(80, 50, 50, 50, 50), "Servidor crítico"
    assert avaliar_datacenter(50, 50, 50, 150, 50),"Servidor em alerta"
    assert avaliar_datacenter(30, 30, 30, 30, 50), "Servidor estável"
import pandas as pd

# === PRODUÇÃO - UVA MESA ===
URL_PRODUCAO_UVA_MESA = "http://vitibrasil.cnpuv.embrapa.br/download/Producao/ProducUvaMesa.csv"
FALLBACK_PRODUCAO_UVA_MESA_CSV = "fallback_producao_uva_mesa.csv"

def buscar_dados_producao_uva_mesa_online():
    try:
        df = pd.read_csv(URL_PRODUCAO_UVA_MESA, sep=';', encoding='latin1', timeout=10)
        df.to_csv(FALLBACK_PRODUCAO_UVA_MESA_CSV, index=False, sep=';', encoding='latin1')
        return df
    except Exception as e:
        print(f"Erro Produção Online: {e}")
        return None

def carregar_dados_producao_uva_mesa_fallback():
    try:
        return pd.read_csv(FALLBACK_PRODUCAO_UVA_MESA_CSV, sep=';', encoding='latin1')
    except Exception as e:
        print(f"Erro Fallback Produção: {e}")
        return None

# === PROCESSAMENTO ===
URL_PROCESSAMENTO = "http://vitibrasil.cnpuv.embrapa.br/download/Processa/Processa.csv"
FALLBACK_PROCESSAMENTO_CSV = "fallback_processamento.csv"

def buscar_dados_processamento_online():
    try:
        df = pd.read_csv(URL_PROCESSAMENTO, sep=';', encoding='latin1', timeout=10)
        df.to_csv(FALLBACK_PROCESSAMENTO_CSV, index=False, sep=';', encoding='latin1')
        return df
    except Exception as e:
        print(f"Erro Processamento Online: {e}")
        return None

def carregar_dados_processamento_fallback():
    try:
        return pd.read_csv(FALLBACK_PROCESSAMENTO_CSV, sep=';', encoding='latin1')
    except Exception as e:
        print(f"Erro Fallback Processamento: {e}")
        return None

# === COMERCIALIZAÇÃO ===
URL_COMERCIALIZACAO = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio/Comercio.csv"
FALLBACK_COMERCIALIZACAO_CSV = "fallback_comercializacao.csv"

def buscar_dados_comercializacao_online():
    try:
        df = pd.read_csv(URL_COMERCIALIZACAO, sep=';', encoding='latin1', timeout=10)
        df.to_csv(FALLBACK_COMERCIALIZACAO_CSV, index=False, sep=';', encoding='latin1')
        return df
    except Exception as e:
        print(f"Erro Comercialização Online: {e}")
        return None

def carregar_dados_comercializacao_fallback():
    try:
        return pd.read_csv(FALLBACK_COMERCIALIZACAO_CSV, sep=';', encoding='latin1')
    except Exception as e:
        print(f"Erro Fallback Comercialização: {e}")
        return None

# === IMPORTAÇÃO (Placeholder) ===
def buscar_dados_importacao_online():
    print("Importação online não implementada.")
    return None

def carregar_dados_importacao_fallback():
    print("Fallback de importação não implementado.")
    return None

# === EXPORTAÇÃO (Placeholder) ===
def buscar_dados_exportacao_online():
    print("Exportação online não implementada.")
    return None

def carregar_dados_exportacao_fallback():
    print("Fallback de exportação não implementado.")
    return None

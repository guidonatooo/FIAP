import pandas as pd

# Caminhos fixos dos arquivos .csv (todos na pasta 'dados')
CAMINHOS_CSV = {
    "producao": "dados/producao.csv",
    "processamento": "dados/processamento.csv",
    "comercializacao": "dados/comercializacao.csv",
    "importacao": "dados/importacao.csv",
    "exportacao": "dados/exportacao.csv"
}

def carregar_csv_local(nome_chave):
    caminho = CAMINHOS_CSV.get(nome_chave)
    if not caminho:
        print(f"[ERRO] Caminho não definido para: {nome_chave}")
        return None
    try:
        df = pd.read_csv(caminho, sep=";", encoding="latin1")
        return df
    except Exception as e:
        print(f"[ERRO] Falha ao carregar {caminho}: {e}")
        return None

# Funções específicas que usam a função genérica
def carregar_dados_producao():
    return carregar_csv_local("producao")

def carregar_dados_processamento():
    return carregar_csv_local("processamento")

def carregar_dados_comercializacao():
    return carregar_csv_local("comercializacao")

def carregar_dados_importacao():
    return carregar_csv_local("importacao")

def carregar_dados_exportacao():
    return carregar_csv_local("exportacao")

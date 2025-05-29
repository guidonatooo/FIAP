import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

DADOS_DIR = os.path.join(PROJECT_ROOT, 'dados')

CAMINHOS_CSV = {
    "producao": os.path.join(DADOS_DIR, "producao.csv"),
    "processamento": os.path.join(DADOS_DIR, "processamento.csv"),
    "comercializacao": os.path.join(DADOS_DIR, "comercializacao.csv"),
    "importacao": os.path.join(DADOS_DIR, "importacao.csv"),
    "exportacao": os.path.join(DADOS_DIR, "exportacao.csv")
}

def carregar_csv_local(nome_chave):
    caminho = CAMINHOS_CSV.get(nome_chave)
    if not caminho:
        print(f"[AVISO] Caminho não definido para a chave: {nome_chave} no dicionário CAMINHOS_CSV.")
        return None

    if not os.path.exists(caminho):
        print(f"[ERRO] Arquivo CSV não encontrado em: {caminho}")
        return None

    try:
        df = pd.read_csv(caminho, sep=";", encoding="latin1")
        return df
    except Exception as e:
        print(f"[ERRO] Falha ao carregar o arquivo CSV {caminho}. Detalhe do erro: {e}")
        return None

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
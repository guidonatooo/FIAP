import pandas as pd

# URL específico para a produção de uvas de mesa
URL_PRODUCAO_UVA_MESA = "http://vitibrasil.cnpuv.embrapa.br/download/Producao/ProducUvaMesa.csv"
# Caminho para guardar/ler o ficheiro de fallback para este dado específico
FALLBACK_PRODUCAO_UVA_MESA_CSV = "fallback_producao_uva_mesa.csv"

def buscar_dados_producao_uva_mesa_online():
    """
    Tenta buscar os dados de produção de uvas de mesa diretamente do site da Embrapa.
    Retorna um DataFrame do pandas ou None se falhar.
    """
    print(f"Tentando buscar dados de produção de uva de mesa online de: {URL_PRODUCAO_UVA_MESA}")
    try:
        # Especificar timeout para não ficar preso indefinidamente
        df = pd.read_csv(URL_PRODUCAO_UVA_MESA, sep=';', encoding='latin1', timeout=10)
        print("Dados de produção de uva de mesa obtidos online com sucesso!")
        # Salvar uma cópia local para o fallback após o sucesso
        df.to_csv(FALLBACK_PRODUCAO_UVA_MESA_CSV, index=False, sep=';', encoding='latin1')
        print(f"Fallback salvo em {FALLBACK_PRODUCAO_UVA_MESA_CSV}")
        return df
    except Exception as e:
        print(f"Erro ao buscar dados de produção de uva de mesa online: {e}")
        return None

def carregar_dados_producao_uva_mesa_fallback():
    """
    Carrega os dados de produção de uvas de mesa do ficheiro CSV de fallback local.
    Retorna um DataFrame do pandas ou None se o ficheiro não for encontrado.
    """
    print(f"Tentando carregar dados de produção de uva de mesa do fallback: {FALLBACK_PRODUCAO_UVA_MESA_CSV}")
    try:
        df = pd.read_csv(FALLBACK_PRODUCAO_UVA_MESA_CSV, sep=';', encoding='latin1')
        print("Dados de produção de uva de mesa carregados do fallback com sucesso!")
        return df
    except FileNotFoundError:
        print(f"Erro: Ficheiro de fallback {FALLBACK_PRODUCAO_UVA_MESA_CSV} não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar dados do fallback {FALLBACK_PRODUCAO_UVA_MESA_CSV}: {e}")
        return None
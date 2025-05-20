from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests

# Importar as funções do nosso módulo extrator
from extrator_embrapa import (
    buscar_dados_producao_uva_mesa_online,
    carregar_dados_producao_uva_mesa_fallback
)

app = FastAPI(
    title="API de Dados Vitivinícolas da Embrapa",
    description="Uma API para consultar dados de produção, processamento, comercialização, importação e exportação da Embrapa.",
    version="0.1.0"
)

EMBRAPA_SITE_URL = "http://vitibrasil.cnpuv.embrapa.br/"

def check_site_online(url, timeout=5):
    """Verifica se um URL está acessível."""
    try:
        response = requests.head(url, timeout=timeout)
        return response.status_code == 200
    except requests.RequestException:
        return False

@app.get("/")
async def root():
    return {"mensagem": "Bem-vindo à API de Dados Vitivinícolas da Embrapa!"}

@app.get("/producao/uvas-mesa", tags=["Produção"])
async def get_producao_uvas_mesa():
    
    """
    Retorna os dados de produção de uvas de mesa.
    Tenta buscar os dados ao vivo do site da Embrapa. Se falhar ou o site estiver offline,
    tenta retornar dados de um fallback local.
    """
    
    
    dados_df = None # DataFrame do Pandas
    origem_dados = ""

    if check_site_online(EMBRAPA_SITE_URL): # Verifica o site principal primeiro
        print("Site da Embrapa parece estar online. Tentando scraping ao vivo...")
        dados_df = buscar_dados_producao_uva_mesa_online()
        if dados_df is not None:
            origem_dados = "Embrapa (ao vivo)"
        else:
            print("Falha no scraping ao vivo. Tentando fallback.")
    else:
        print("Site da Embrapa parece estar offline. Tentando fallback local.")

    if dados_df is None: # Se o scraping ao vivo falhou ou site offline
        dados_df = carregar_dados_producao_uva_mesa_fallback()
        if dados_df is not None:
            origem_dados = "Fallback local (CSV)"
    
    if dados_df is not None:
        # Converter o DataFrame para uma lista de dicionários (formato JSON)
        return {
            "status": "sucesso",
            "origem_dados": origem_dados,
            "dados": dados_df.to_dict(orient="records")
        }
    else:
        # Se ambos falharem (ao vivo e fallback)
        raise HTTPException(
            status_code=503, 
            detail={
                "status": "erro",
                "mensagem": "Site da Embrapa indisponível e dados de fallback não encontrados para produção de uvas de mesa."
            }
        )

# --- Adicionar outros endpoints aqui para outras categorias e subcategorias ---
# Exemplo:
# @app.get("/producao/vinhos-mesa", tags=["Produção"])
# async def get_producao_vinhos_mesa():
#     # Lógica similar para buscar/carregar dados de vinhos de mesa
#     pass

# @app.get("/processamento/viniferas", tags=["Processamento"])
# async def get_processamento_viniferas():
#     # Lógica para dados de processamento
#     pass
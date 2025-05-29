from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests
import pandas as pd

from antigo_extratores_embrapa import (
    buscar_dados_producao_uva_mesa_online,
    carregar_dados_producao_uva_mesa_fallback,
    buscar_dados_processamento_online,
    carregar_dados_processamento_fallback,
    buscar_dados_comercializacao_online,
    carregar_dados_comercializacao_fallback,
    buscar_dados_importacao_online,
    carregar_dados_importacao_fallback,
    buscar_dados_exportacao_online,
    carregar_dados_exportacao_fallback
)

app = FastAPI(
    title="API de Dados Vitivinícolas da Embrapa",
    description="Uma API para consultar dados de produção, processamento, comercialização, importação e exportação da Embrapa.",
    version="0.1.0"
)

EMBRAPA_SITE_URL = "http://vitibrasil.cnpuv.embrapa.br/"

def check_site_online(url, timeout=5):
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
    return obter_dados_padrao(
        check_site_online(EMBRAPA_SITE_URL),
        buscar_dados_producao_uva_mesa_online,
        carregar_dados_producao_uva_mesa_fallback,
        "produção de uvas de mesa"
    )

@app.get("/processamento", tags=["Processamento"])
async def get_processamento():
    return obter_dados_padrao(
        check_site_online(EMBRAPA_SITE_URL),
        buscar_dados_processamento_online,
        carregar_dados_processamento_fallback,
        "processamento de uvas"
    )

@app.get("/comercializacao", tags=["Comercialização"])
async def get_comercializacao():
    return obter_dados_padrao(
        check_site_online(EMBRAPA_SITE_URL),
        buscar_dados_comercializacao_online,
        carregar_dados_comercializacao_fallback,
        "comercialização de produtos vitivinícolas"
    )

@app.get("/importacao", tags=["Importação"])
async def get_importacao():
    return obter_dados_padrao(
        check_site_online(EMBRAPA_SITE_URL),
        buscar_dados_importacao_online,
        carregar_dados_importacao_fallback,
        "importação de produtos vitivinícolas"
    )

@app.get("/exportacao", tags=["Exportação"])
async def get_exportacao():
    return obter_dados_padrao(
        check_site_online(EMBRAPA_SITE_URL),
        buscar_dados_exportacao_online,
        carregar_dados_exportacao_fallback,
        "exportação de produtos vitivinícolas"
    )

def obter_dados_padrao(site_online, buscar_online_fn, fallback_fn, descricao):
    dados_df = None
    origem_dados = ""

    if site_online:
        print(f"Site da Embrapa online. Tentando scraping ao vivo para {descricao}...")
        dados_df = buscar_online_fn()
        if dados_df is not None:
            origem_dados = "Embrapa (ao vivo)"
        else:
            print("Falha no scraping ao vivo. Tentando fallback.")
    else:
        print("Site da Embrapa offline. Tentando fallback local.")

    if dados_df is None:
        dados_df = fallback_fn()
        if dados_df is not None:
            origem_dados = "Fallback local (CSV)"

    if dados_df is not None:
        return {
            "status": "sucesso",
            "origem_dados": origem_dados,
            "dados": dados_df.to_dict(orient="records")
        }
    else:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "erro",
                "mensagem": f"Site da Embrapa indisponível e dados de fallback não encontrados para {descricao}."
            }
        )
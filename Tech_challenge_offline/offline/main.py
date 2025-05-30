from fastapi import FastAPI, HTTPException
import pandas as pd

from extratores_embrapa import (
    carregar_dados_producao,
    carregar_dados_processamento,
    carregar_dados_comercializacao,
    carregar_dados_importacao,
    carregar_dados_exportacao
)

app = FastAPI(
    title="API de Dados Vitivinícolas da Embrapa (Versão Offline)",
    description="API baseada em arquivos locais CSV devido à indisponibilidade do site da Embrapa.",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"mensagem": "API de Dados Vitivinícolas da Embrapa - versão offline (dados locais)"}


@app.get("/producao", tags=["Produção"])
async def get_producao():
    return responder_dados(carregar_dados_producao(), "produção de uvas")

@app.get("/processamento", tags=["Processamento"])
async def get_processamento():
    return responder_dados(carregar_dados_processamento(), "processamento de uvas")

@app.get("/comercializacao", tags=["Comercialização"])
async def get_comercializacao():
    return responder_dados(carregar_dados_comercializacao(), "comercialização de produtos")

@app.get("/importacao", tags=["Importação"])
async def get_importacao():
    return responder_dados(carregar_dados_importacao(), "importação de produtos")

@app.get("/exportacao", tags=["Exportação"])
async def get_exportacao():
    return responder_dados(carregar_dados_exportacao(), "exportação de produtos")


def responder_dados(dados_df, descricao):
    """
    Respostas e mensagens de erro
    """
    if dados_df is not None:
        return {
            "status": "sucesso",
            "origem_dados": "Arquivo local (.csv)",
            "dados": dados_df.to_dict(orient="records")
        }
    else:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "erro",
                "mensagem": f"Erro ao carregar dados locais de {descricao}."
            }
        )

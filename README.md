# API de Dados Vitivinícolas da Embrapa

Este projeto é parte do **Tech Challenge – Fase 1** do curso de **Machine Learning Engineering da FIAP**.  
A aplicação consiste em uma **API REST em Python (FastAPI)** para consulta de dados de vitivinicultura disponibilizados pela **Embrapa** em tempo real, com fallback local para casos de instabilidade.

---

## Link de Deploy
🔗 [Acesse a API ao vivo](https://stunning-fiesta-5gv4gpjj696qcvpwg-8000.app.github.dev)

---

## ✅ Funcionalidades

- Raspagem de dados ao vivo do site da Embrapa
- Fallback automático para arquivos `.csv` locais caso o site esteja fora do ar
- Endpoints separados por tema
- Documentação automática (Swagger)

---

## Endpoints Disponíveis

| Método | Rota                       | Descrição                                    |
|--------|----------------------------|----------------------------------------------|
| GET    | `/`                        | Mensagem de boas-vindas                      |
| GET    | `/producao/uvas-mesa`      | Produção de uvas de mesa                     |
| GET    | `/processamento`           | Dados de processamento                       |
| GET    | `/comercializacao`         | Comercialização de produtos vitivinícolas    |
| GET    | `/importacao`              | Importação *(placeholder)*                   |
| GET    | `/exportacao`              | Exportação *(placeholder)*                   |
| GET    | `/docs`                    | Swagger UI para testes interativos           |

---

## Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/guidonatooo/FIAP
cd FIAP

---

### 2. Instale as dependências

```bash
pip install -r requirements.txt

---

## Rodar API

uvicorn main:app --reload

---
## Estrutura de Pastas

/dados/
├── comercializacao.csv
├── exportacao.csv
├── importacao.csv
├── processamento.csv
└── producao.csv

Tech_challenge/
│
├── main.py                     # Código principal da API
├── extratores_embrapa.py       # Lógica de scraping e fallback
├── fallback_*.csv              # Arquivos locais para fallback
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo

---

## Arquitetura

[FastAPI]
   │
   ├─ Verifica se o site da Embrapa está online
   │     ├─ Se SIM → Raspagem com pandas
   │     └─ Se NÃO → Carrega fallback CSV local
   │
Retorna JSON para o cliente

---

## Apresentação (video)

---

### Contribuição & Manutenção

Este projeto foi desenvolvido individualmente por Guilherme para fins educacionais.
Contribuições e melhorias são bem-vindas!

---
## Extras

Este projeto inicialmente implementava raspagem de dados diretamente do site da Embrapa.  
No entanto, como o site está atualmente fora do ar, a API foi adaptada para operar 100% com arquivos locais.  

Scripts de raspagem originais podem ser encontrados em:
- Raspa_Comercializacao.ipynb
- Raspa_Exportacao.ipynb
- Raspa_Importacao.ipynb
- Raspa_Processamento.ipynb
- Raspa_Producao.ipynb

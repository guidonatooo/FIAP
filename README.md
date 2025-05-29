```markdown
# API de Dados Vitivinícolas da Embrapa — Versão Offline

Este projeto foi desenvolvido como parte do **Tech Challenge – Fase 1** do curso de **Machine Learning Engineering da FIAP**.

A proposta é uma **API REST** desenvolvida em **Python com FastAPI**, que permite consultar dados da vitivinicultura brasileira.  
Devido à indisponibilidade do site oficial da Embrapa, todos os dados são servidos via **arquivos locais `.csv`** previamente baixados.

---

## 🚀 Link da API (GitHub Codespaces)

🔗 [Acesse a API ao vivo](https://obscure-spork-97wrxjprq952xjqj.github.dev/)

---

## ✅ Funcionalidades

- Fornece dados de produção, processamento, comercialização, importação e exportação de produtos vitivinícolas
- Utiliza arquivos `.csv` armazenados localmente
- Endpoints bem definidos
- Swagger UI disponível em `/docs`
- Organização modular (`main.py` + `extratores_embrapa.py`)

---

## 📂 Estrutura de Pastas

```

Tech\_challenge/
├── dados/                      # Arquivos CSV utilizados
│   ├── producao.csv
│   ├── processamento.csv
│   ├── comercializacao.csv
│   ├── importacao.csv
│   └── exportacao.csv
│
├── extratores\_embrapa.py       # Funções de leitura dos CSVs
├── main.py                     # Endpoints da API
├── requirements.txt            # Dependências do projeto
├── README.md
├── Diagrama.png                # Arquitetura da API
└── Raspa\_\*.ipynb               # Notebooks antigos de raspagem (extras)

````

---

## 📌 Endpoints disponíveis

| Método | Rota               | Descrição                              |
|--------|--------------------|----------------------------------------|
| GET    | `/`                | Mensagem de boas-vindas                |
| GET    | `/producao`        | Produção de uvas                       |
| GET    | `/processamento`   | Dados de processamento                 |
| GET    | `/comercializacao` | Comercialização de produtos            |
| GET    | `/importacao`      | Dados de importação                    |
| GET    | `/exportacao`      | Dados de exportação                    |
| GET    | `/docs`            | Interface Swagger para testes          |

---

## 🧱 Stack utilizada

- Python 3.11+
- FastAPI
- Uvicorn
- Pandas

---

## ⚙️ Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/guidonatooo/FIAP
````

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
```

#### Ativando o ambiente:

* **Linux/macOS ou GitHub Codespaces**:

```bash
source .venv/bin/activate
```

* **Windows (cmd ou PowerShell)**:

```bash
.venv\Scripts\activate
```

⚠️ **Atenção**: No GitHub Codespaces, ative o ambiente com `source .venv/bin/activate`, pois o caminho do Windows **não funciona** no terminal bash.

Como confirmação observe (.venv) @guidonatooo ➜ /workspaces/FIAP (main) $

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Inicie a API

```bash
uvicorn main:app --reload
```

## 🧪 Extras: Notebooks de raspagem

Inicialmente, este projeto utilizava scraping direto do site da Embrapa.
Por conta da indisponibilidade do portal, os dados passaram a ser fornecidos apenas via arquivos `.csv`.

Os scripts de raspagem estão disponíveis na raiz como documentação técnica adicional:

* `Raspa_Producao.ipynb`
* `Raspa_Processamento.ipynb`
* `Raspa_Comercializacao.ipynb`
* `Raspa_Importacao.ipynb`
* `Raspa_Exportacao.ipynb`

---

## 🗺️ Diagrama de arquitetura

![Diagrama da Solução](./Diagrama.jpg)

---

## 🎥 Vídeo de apresentação

🔗 [Assista ao vídeo aqui](https://SEU-LINK-DO-VIDEO)

---

## 👨‍💻 Autor

Guilherme Donato – [LinkedIn](https://www.linkedin.com/in/)

---

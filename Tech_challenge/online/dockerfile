# Imagem base
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro da imagem
COPY . /app

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pelo Uvicorn
EXPOSE 10000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:10000"]



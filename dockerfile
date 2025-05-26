# Usar uma imagem base oficial do Python
FROM python:3.13-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY pyproject.toml poetry.lock* /app/

# Instala as dependências do projeto
RUN pip install --upgrade pip \
    && pip install .

# Copia o código da aplicação para o container
COPY . /app

# Comando padrão para rodar a aplicação (pode ser alterado)
CMD ["python", "main.py"]

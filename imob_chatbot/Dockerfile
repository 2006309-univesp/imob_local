# Usa uma imagem do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . /app

# Instala as dependências
RUN pip install -r requirements.txt

# Executa a aplicação
CMD ["python", "run.py"]
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
PROJECT_ID = os.getenv("PROJECT_ID")
SCOPES = ["https://www.googleapis.com/auth/dialogflow"]
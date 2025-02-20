import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

class Config:
    MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')


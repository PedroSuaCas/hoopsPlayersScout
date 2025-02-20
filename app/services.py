import os
from mistralai.models.chat_completion import ChatMessage
from mistralai.client import MistralClient
from .config import Config

# Inicializar cliente de Mistral AI
client = MistralClient(api_key=Config.MISTRAL_API_KEY)

def interpret_query(query):
    try:
        # Crear la lista de mensajes correctamente
        messages = [ChatMessage(role="user", content=query)]
        
        # Hacer la solicitud al modelo de Mistral
        response = client.chat(model="mistral-medium", messages=messages)

        # Acceder correctamente a la respuesta
        return response.choices[0].message.content  # Acceder al contenido del mensaje

    except Exception as e:
        return f"Ocurrió un error con Mistral: {str(e)}"

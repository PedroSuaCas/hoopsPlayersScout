from openai import OpenAI
import openai
from .config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)
client = OpenAI(organization=Config.OPENAI_ORG_ID)


# Inicializa la API de OpenAI con la clave de configuración

def interpret_query(query):
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                   messages=[{"role": "user", "content": query}])
        return response.choices[0].message.content
    #except openai.RateLimitError:
    #    return "Has superado tu cuota de uso. Por favor, intenta más tarde."
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"
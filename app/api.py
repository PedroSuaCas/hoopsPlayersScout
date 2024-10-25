import openai
import os
from dotenv import load_dotenv
from fastapi import HTTPException

#Business Logic of endpoints

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def consulta_jugador(nombre_jugador: str):
    prompt = f"Proporciona información detallada sobre el jugador {nombre_jugador}, incluyendo estadísticas, rendimiento y cualquier dato relevante para scouters y clubes."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"respuesta": response['choices'][0]['message']['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
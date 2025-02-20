from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import requests
import os
from bs4 import BeautifulSoup

sportradar_api_key = os.getenv("SPORTRADAR_API_KEY")

def interpret_query_with_gpt(query):
    """
    Envía la consulta al modelo GPT para interpretación.
    """
    response = client.completions.create(engine="gpt-4",  # Cambia a "text-davinci-003" si prefieres GPT-3
    prompt=f"Analiza y responde esta consulta de baloncesto: {query}",
    max_tokens=100)
    return response.choices[0].text.strip()

def fetch_basketball_stats(query_type, params):
    """
    Usa una API externa para obtener estadísticas de baloncesto.
    query_type: "player", "team", "competition" 
    params: diccionario con parámetros de consulta.
    """
    if query_type == "player":
        return fetch_player_stats(params)
    elif query_type == "team":
        return fetch_team_stats(params)
    elif query_type == "competition":
        return fetch_competition_stats(params)

def fetch_player_stats(params):
    """
    Realiza scraping en Basketball Reference para estadísticas de jugadores.
    """
    player_name = params.get("name")
    url = f"https://www.basketball-reference.com/search/search.fcgi?search={player_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    stats = {
        "points": "No disponible",
        "rebounds": "No disponible",
        "assists": "No disponible"
    }

    # Ejemplo básico de scraping para obtener estadísticas del jugador
    try:
        stats["points"] = soup.select_one("#per_game .p_per_game").text
        stats["rebounds"] = soup.select_one("#per_game .r_per_game").text
        stats["assists"] = soup.select_one("#per_game .a_per_game").text
    except Exception as e:
        print("Error al extraer estadísticas:", e)

    return stats

def fetch_team_stats(params):
    """
    Consulta la API de Sportradar para estadísticas de equipos.
    """
    team_id = params.get("team_id")
    url = f"https://api.sportradar.us/basketball/trial/v4/en/teams/{team_id}/profile.json?api_key={sportradar_api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "No se pudo obtener los datos del equipo"}

def handle_user_query(user_query):
    """
    Procesa la consulta del usuario usando GPT y recupera datos de baloncesto.
    """
    gpt_response = interpret_query_with_gpt(user_query)

    if "jugador" in user_query.lower():
        # Extraer datos específicos de jugador
        player_params = {"name": extract_name_from_query(user_query)}
        stats = fetch_basketball_stats("player", player_params)
    elif "equipo" in user_query.lower():
        team_params = {"team_id": extract_team_id_from_query(user_query)}
        stats = fetch_basketball_stats("team", team_params)
    else:
        stats = {"error": "No se pudo interpretar la consulta"}

    return {
        "gpt_response": gpt_response,
        "stats": stats
    }

def extract_name_from_query(query):
    # Implementar extracción de nombre para obtener información de jugador
    pass

def extract_team_id_from_query(query):
    # Implementar extracción de ID de equipo según la consulta
    pass

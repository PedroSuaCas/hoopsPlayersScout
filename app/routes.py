from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.api import consulta_jugador
∫
#To create the routes and endpoints o hoopsplayerscoutapp


router = APIRouter()

router.add_api_route("/consulta_jugador/", consulta_jugador, methods=["POST"])
router.mount("/static", StaticFiles(directory="app/static"), name="static")

@router.get("/", response_class=HTMLResponse)
async def get_index():
    with open("app/static/index.html") as f:
        return f.read(
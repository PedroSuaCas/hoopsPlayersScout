from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI()

app.include_router(router)
# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Cambia el método para servir el HTML en la raíz
@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("app/static/index.html") as f:
        return f.read()
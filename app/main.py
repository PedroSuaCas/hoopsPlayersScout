from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Hoops Players Scouts. How can I help you today?"}

app.include_router(router)
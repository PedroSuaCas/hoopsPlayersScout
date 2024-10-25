from fastapi import FastAPI
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Load enviroment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
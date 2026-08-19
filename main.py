import requests
from fastapi import FastAPI

app = FastAPI()

def root():
@app.get("/")
async def index():
   return {"message": "Hello World"}

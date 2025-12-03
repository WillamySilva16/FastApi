from fastapi import FastAPI
from db import buscar_visitas  # importa função que pega dados do BD

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API online!"}

@app.get("/visitas")
def listar_visitas():
    dados = buscar_visitas()
    return dados

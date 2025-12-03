from fastapi import APIRouter
from app.db import buscar_visitas

router = APIRouter()

@router.get("/visitas")
def listar_visitas():
    return buscar_visitas()

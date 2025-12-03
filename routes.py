from fastapi import APIRouter
from db import get_connection

router = APIRouter()

@router.get("/visitas")
def get_visitas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO")
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    data = [dict(zip(columns, row)) for row in rows]

    return {"rows": data}

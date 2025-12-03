import pyodbc

def buscar_visitas():
    server = "pbdb3073.database.windows.net"
    database = "PBDB3073"
    username = "admrs"
    password = "Gf3$Rn8!Qb12^KsW0tZ"  # coloque a senha que usa no SQLDBX

    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("SELECT TOP 100 * FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO")

    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    
    return results

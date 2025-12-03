import pyodbc

def get_connection():
    server = "pbdb3073.database.windows.net"
    database = "PBDB3073"
    username = "admrs"
    password = "Gf3$Rn8!Qb12^KsW0tZ"  # depois colocamos isso em variável de ambiente no Railway
    
    connection_string = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    )

    return pyodbc.connect(connection_string)

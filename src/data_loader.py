import pandas as pd
import pyodbc

def connect_to_sql_server():
    """
    Cria conexão com o banco de dados SQL Server.
    """
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=MODELOS_PREDITIVOS;'
            'UID=usuario_python;'
            'PWD=123456;'
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None

def load_data(query: str) -> pd.DataFrame:
    """
    Executa uma query e retorna um DataFrame com os dados.
    """
    conn = connect_to_sql_server()
    if conn:
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    return pd.DataFrame()

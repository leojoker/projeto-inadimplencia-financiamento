def truncate_table(conn, table_name: str):
    """
    Trunca a tabela informada no banco de dados.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(f"TRUNCATE TABLE {table_name}")
        conn.commit()
        print(f"Tabela {table_name} truncada com sucesso.")
    except Exception as e:
        print(f"Erro ao truncar a tabela {table_name}: {e}")

def inserir_previsoes(conn, df_resultados, tabela_destino: str):
    """
    Insere as previsões na tabela especificada.
    """
    try:
        cursor = conn.cursor()
        for _, row in df_resultados.iterrows():
            sql = f"INSERT INTO {tabela_destino} (NUMERO_CONTRATO, PREVISOES, PROBABILIDADES) VALUES (?, ?, ?)"
            cursor.execute(sql, (row['NUMERO_CONTRATO'], row['PREVISOES'], row['PROBABILIDADES']))
        conn.commit()
        print("Dados inseridos com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

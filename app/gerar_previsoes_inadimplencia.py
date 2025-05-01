import pandas as pd
from src.data_loader import connect_to_sql_server, load_data
from src.preprocessing import transformar_variaveis, preparar_dados_para_modelo
from src.predictor import carregar_modelo, gerar_previsoes
from src.sql_utils import truncate_table, inserir_previsoes

def gerar_previsoes_inadimplencia():
    print("Iniciando pipeline de previsões...")

    # Conexão com banco e truncamento da tabela
    conn = connect_to_sql_server()
    if not conn:
        print("Falha na conexão com o banco.")
        return

    truncate_table(conn, "dbo.RESULTADOS_INTERMEDIARIO")

    # Carregamento dos dados
    print("Carregando dados do banco...")
    query = "SELECT * FROM EXTRACAO_DADOS_SISTEMA"
    df = load_data(query)
    df.dropna(inplace=True)

    # Feature engineering
    df = transformar_variaveis(df)

    # Colunas usadas pelo modelo
    colunas_modelo = [
        'TAXA_AO_ANO', 'CIDADE_CLIENTE', 'ESTADO_CLIENTE', 'RENDA_MENSAL_CLIENTE',
        'QT_PC_ATRASO', 'QT_DIAS_PRIM_PC_ATRASO', 'QT_TOTAL_PC_PAGAS', 'VL_TOTAL_PC_PAGAS',
        'QT_PC_PAGA_EM_DIA', 'QT_DIAS_MIN_ATRASO', 'QT_DIAS_MAX_ATRASO',
        'QT_DIAS_MEDIA_ATRASO', 'VALOR_PARCELA', 'IDADE_DATA_ASSINATURA_CONTRATO',
        'FAIXA_VALOR_FINANCIADO', 'FAIXA_PRAZO_FINANCIAMENTO'
    ]

    dados_normalizados = preparar_dados_para_modelo(df, colunas_modelo)

    # Previsão
    print("Carregando modelo...")
    modelo = carregar_modelo("models/modelo_treinado.pk")
    previsoes, probabilidades = gerar_previsoes(modelo, dados_normalizados)

    # Preparar dataframe final
    df['PREVISOES'] = previsoes
    df['PROBABILIDADES'] = probabilidades
    df_resultados = df[['NUMERO_CONTRATO', 'PREVISOES', 'PROBABILIDADES']]

    # Inserir no banco
    inserir_previsoes(conn, df_resultados, "dbo.RESULTADOS_INTERMEDIARIO")

    # Fechar conexão
    conn.close()

    print("Previsões geradas e armazenadas com sucesso.")

def main():
    gerar_previsoes_inadimplencia()

if __name__ == "__main__":
    main()

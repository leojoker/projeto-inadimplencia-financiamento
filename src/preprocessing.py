import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def transformar_variaveis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria variáveis derivadas de prazo e valor financiado.
    """
    df['FAIXA_PRAZO_FINANCIAMENTO'] = pd.cut(
        df['PZ_FINANCIAMENTO'], bins=[-100, 120, 180, 240],
        labels=['Até 120 Meses', '121 até 180 Meses', '181 até 240 Meses'])

    df['FAIXA_VALOR_FINANCIADO'] = pd.cut(
        df['VALOR_FINANCIAMENTO'],
        bins=[-100, 100_000, 200_000, 300_000, 400_000, 500_000, 750_000, 1_000_000, 9e9],
        labels=['Até 100 mil', '101 até 200 mil', '201 até 300 mil',
                '301 até 400 mil', '401 até 500 mil', '501 até 750 mil',
                'De 751 até 1.000.000', 'Mais de 1.000.000'])
    return df

def preparar_dados_para_modelo(df: pd.DataFrame, colunas_modelo: list) -> pd.DataFrame:
    """
    Codifica variáveis categóricas e normaliza os dados.
    """
    df_modelo = df[colunas_modelo].copy()

    for col in df_modelo.select_dtypes(include=['object', 'category']).columns:
        df_modelo[col] = LabelEncoder().fit_transform(df_modelo[col])

    dados_normalizados = MinMaxScaler().fit_transform(df_modelo)
    return dados_normalizados

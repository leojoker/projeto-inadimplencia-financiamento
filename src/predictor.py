import joblib

def carregar_modelo(caminho_modelo):
    """
    Carrega modelo treinado com joblib.
    """
    return joblib.load(caminho_modelo)

def gerar_previsoes(modelo, dados_normalizados):
    """
    Gera previsões e probabilidades com o modelo carregado.
    """
    previsoes = modelo.predict(dados_normalizados)
    probabilidades = modelo.predict_proba(dados_normalizados)[:, 1]
    return previsoes, probabilidades

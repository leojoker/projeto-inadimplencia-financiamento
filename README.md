# Projeto de Previsão de Inadimplência

Este projeto tem como objetivo desenvolver uma pipeline completa de ciência de dados para prever inadimplência de contratos financeiros. O modelo é baseado em dados reais extraídos de um sistema e utiliza técnicas de engenharia de atributos, normalização e machine learning.

---

## 🔍 Estrutura do Projeto

```
PROJETO_INADIMPLENCIA/
├── app/                            # Script principal da pipeline
│   └── gerar_previsoes_inadimplencia.py
├── data/                           # Diretórios para armazenamento de dados
│   ├── raw/                        # Dados brutos
│   ├── processed/                 # Dados tratados
│   └── final/                     # Resultados finais
├── models/                         # Modelos treinados (.pkl)
├── notebooks/                      # Análises e desenvolvimento exploratório
│   ├── 01_Exploracao.ipynb
│   ├── 02_Preprocessamento.ipynb
│   ├── 03_Treinamento_Modelo.ipynb
│   ├── 04_Avaliacao_Modelo.ipynb
│   └── 05_Deploy_Pipeline.ipynb
├── src/                            # Código modular reutilizável
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model_trainer.py
│   ├── predictor.py
│   └── sql_utils.py
├── tests/                          # Testes automatizados (em desenvolvimento)
│   └── test_model.py
├── requirements.txt                # Bibliotecas necessárias
└── README.md                       # Este arquivo
```

---

## ⚙️ Etapas da Pipeline

1. **Exploração de Dados:** visualização e entendimento dos dados.
2. **Pré-processamento:** criação de variáveis derivadas, tratamento e normalização.
3. **Treinamento do Modelo:** uso de Random Forest para aprendizado supervisionado.
4. **Avaliação:** métricas como Acurácia, Precisão, Recall e F1-Score.
5. **Deploy e Integração:** inserção das previsões no banco de dados SQL Server.

---

## 🚀 Como Executar

1. Instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

2. Execute a pipeline:
```bash
python app/gerar_previsoes_inadimplencia.py
```

---

## 🧠 Modelo

- Algoritmo: `RandomForestClassifier`
- Normalização: `MinMaxScaler`
- Codificação: `LabelEncoder`
- Armazenamento de modelo: `joblib`

---

## 💾 Banco de Dados

O projeto se conecta a um banco SQL Server via `pyodbc` para extrair dados e armazenar previsões.

---

## ✍️ Autor

Desenvolvido por Leonardo Barbosa — Cientista de Dados com foco em projetos aplicados à área financeira e Futebol.

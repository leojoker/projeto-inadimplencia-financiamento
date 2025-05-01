# 📊 Projeto de Previsão de Inadimplência em Financiamentos

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org)
[![Licença MIT](https://img.shields.io/badge/Licença-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)]()

Este projeto implementa uma pipeline completa de Ciência de Dados com foco na previsão de inadimplência em financiamentos. A solução é estruturada de ponta a ponta: desde a extração dos dados até a geração das previsões e integração com o banco de dados.

---

## 🚀 Tecnologias Utilizadas

- Python 3.13
- Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib
- SQL Server com PyODBC
- Jupyter Notebooks
- Joblib
- SMOTE (balanceamento)
- Git + GitHub

---

## 🧱 Estrutura do Projeto

```
PROJETO_INADIMPLENCIA/
├── notebooks/                  # Jupyter Notebooks com cada etapa da pipeline
│   ├── 01_Exploracao.ipynb
│   ├── 02_Preprocessamento.ipynb
│   ├── 03_04_Treinamento_Avaliacao_Modelo.ipynb
│   └── 05_Deploy_Pipeline.ipynb
├── src/                        # Módulos Python reutilizáveis
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model_trainer.py
│   ├── predictor.py
│   └── sql_utils.py
├── app/                        # Script de execução da pipeline
│   └── gerar_previsoes_inadimplencia.py
├── data/                       # Dados locais organizados
│   ├── raw/
│   ├── processed/
│   └── final/
├── models/                     # Modelos treinados (.pkl)
├── tests/                      # Testes automatizados
├── requirements.txt            # Dependências do projeto
├── .gitignore                  # Arquivos ignorados pelo Git
└── README.md                   # Este documento
```

---

## 🔎 Pipeline de Desenvolvimento

1. **Exploração de Dados** – Visualização, limpeza inicial e estatísticas descritivas.
2. **Pré-processamento** – Feature engineering, encoding, e preparação.
3. **Treinamento** – Modelo RandomForest balanceado com SMOTE.
4. **Avaliação** – Métricas de performance e importância das variáveis.
5. **Deploy** – Geração de previsões e inserção no banco SQL Server.

---

## 📈 Resultados Esperados

- Classificador com alta acurácia na identificação de contratos inadimplentes.
- Modelo exportado em `.pkl` e integrado com pipeline de banco de dados.
- Gráficos e análises de suporte para tomada de decisão.

---

## 🧪 Como Executar Localmente

```bash
# 1. Clonar o repositório
git clone https://github.com/leojoker/projeto-inadimplencia-financiamento.git
cd projeto-inadimplencia-financiamento

# 2. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar o script principal (ou use os notebooks)
python app/gerar_previsoes_inadimplencia.py
```

---

## 🧠 Autor

**Leonardo Barbosa**  
Cientista de Dados | Projetos em Finanças, Inteligência de Negócios e Machine Learning  
📫 [linkedin.com/in/leonardo-barbosa](https://www.linkedin.com/in/leonardo-barbosa777/)

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

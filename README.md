# 📊 Pipeline de ETL com Prefect – Limpeza de Dados da Netflix

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas)
![Prefect](https://img.shields.io/badge/Prefect-Orchestration-5E60CE?logo=prefect)
![ETL](https://img.shields.io/badge/ETL-Data%20Pipeline-orange)
![Data Engineering](https://img.shields.io/badge/Data%20Engineering-Workflow-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Language](https://img.shields.io/badge/Lang-PT--BR-green)

## 🧾 Descrição do Projeto

Este projeto implementa um **pipeline de ETL (Extract, Transform, Load)** utilizando **Python** e **Prefect** para orquestração de tarefas. O objetivo principal é realizar o processo de **data wrangling** em um dataset de títulos da Netflix, padronizando, limpando e preparando os dados para análises posteriores.

O pipeline inclui monitoramento de execução, registro de logs e validações simples de qualidade de dados, como verificação de valores nulos.

Este projeto foi desenvolvido como estudo prático de **engenharia e preparação de dados**, com foco em boas práticas de organização, modularização e automação de pipelines.

---

## 🎯 Objetivos

* Implementar um pipeline de ETL modular e reutilizável
* Automatizar o fluxo de processamento de dados
* Aplicar técnicas de limpeza e padronização de dados
* Utilizar uma ferramenta de orquestração (Prefect)
* Monitorar a qualidade dos dados durante o processamento
* Simular um fluxo real de preparação de dados para análise

---

## 🧰 Tecnologias Utilizadas

* **Python**
* **Pandas**
* **Prefect** (orquestração de pipelines)
* **CSV** (armazenamento de dados)
* **Logging** (monitoramento de execução)

---

## 🗂️ Estrutura do Projeto

```
project/
│
├── prefect_flow.py      # Orquestração do pipeline com Prefect
├── pipeline.py          # Funções de extração e carga
├── transform.py         # Regras de transformação e limpeza de dados
├── config.py            # Caminhos de entrada e saída
│
├── data/
│   ├── netflix_titles.csv   # Dataset original
│   └── df_limpo.csv         # Dataset após transformação
│
└── logs/
    └── pipeline.log     # Logs de execução do pipeline
```

---

## 🔄 Fluxo do Pipeline (ETL)

### 1. Extract (Extração)

* Leitura do arquivo CSV contendo os dados da Netflix
* Carregamento dos dados em um DataFrame Pandas

Função responsável:

```
extract(csv)
```

---

### 2. Transform (Transformação)

Nesta etapa são aplicadas diversas regras de limpeza e padronização dos dados.

#### Transformações realizadas:

* Remoção da coluna:

  * `description`

* Padronização de nomes de colunas:

  * Conversão para português
  * Uso de nomes mais descritivos

Exemplo:

```
show_id → id
release_year → lancado_em
listed_in → genero
```

* Tratamento de valores nulos:

  * Preenchimento com o valor **"Não informado"** nas colunas:

    * diretor
    * elenco
    * pais

* Limpeza de strings:

  * Remoção de espaços extras na coluna de data

* Conversão de tipos de dados:

  * `adicionado_em` → datetime
  * `lancado_em` → ano (inteiro)

Função principal:

```
transform(df)
```

---

### 3. Load (Carga)

* Salvamento do dataset transformado em um novo arquivo CSV
* Substituição automática do arquivo caso já exista

Função responsável:

```
load(df, output)
```

---

## ⚙️ Orquestração com Prefect

O pipeline é gerenciado por um **flow do Prefect**, que organiza as etapas em tarefas independentes.

Arquivo:

```
prefect_flow.py
```

### Tarefas definidas:

* `extract_task()`
* `transform_task()`
* `load_task()`

O Prefect permite:

* Monitorar a execução do pipeline
* Registrar logs
* Controlar o fluxo de tarefas
* Identificar erros facilmente

---

## 📈 Monitoramento de Qualidade de Dados

Durante a transformação, o pipeline calcula:

* Quantidade total de valores nulos
* Percentual de dados faltantes

Se o percentual de valores nulos ultrapassar **10%**, o sistema gera um alerta:

```
WARNING: Alto volume de valores nulos
```

Isso simula uma prática comum em pipelines reais de dados: **data quality checks**.

---

## ▶️ Como Executar o Projeto

### 0. Pré-requisitos

Para executar este projeto localmente, é necessário ter instalado:

- Python 3.10 ou superior
- pip (gerenciador de pacotes do Python)
- Ambiente virtual (recomendado)

#### Verificando se o Python está instalado:

No terminal, execute:

```
python --version
```

ou

```
python3 --version
```

Se o Python não estiver instalado, faça o download no site oficial:
https://www.python.org/downloads/

---

### 1. Instalar dependências

```
pip install pandas prefect
```

---

### 2. Ajustar os caminhos no arquivo

```
config.py
```

Exemplo:

```
INPUT_PATH = "caminho/para/netflix_titles.csv"
OUTPUT_PATH = "caminho/para/df_limpo.csv"
```

---

### 3. Executar o pipeline

```
python prefect_flow.py
```

Ou executar diretamente o pipeline simples:

```
python pipeline.py
```

---

## 📊 Dataset Utilizado

O Dataset utilizado é o Netflix Movies and TV Shows, disponível no Kaggle:
https://www.kaggle.com/datasets/shivamb/netflix-shows

Principais campos:

* Tipo (Filme ou Série)
* Título
* Diretor
* Elenco
* País
* Data de adição
* Ano de lançamento
* Classificação indicativa
* Duração
* Gênero

---

## 🧠 Possíveis Evoluções do Projeto

Este pipeline pode ser expandido para cenários mais avançados, como:

* Integração com banco de dados (PostgreSQL, MySQL)
* Uso de armazenamento em nuvem (AWS S3, Google Cloud Storage)
* Agendamento automático do pipeline
* Testes automatizados de qualidade de dados
* Versionamento de dados
* Criação de dashboards a partir dos dados tratados
* Implementação de logging estruturado
* Containerização com Docker

---

## 🏷️ Tags

```
ETL
Data Engineering
Data Wrangling
Prefect
Python
Pandas
Data Pipeline
```

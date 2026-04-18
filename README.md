Pipeline ETL com Pandas

Este projeto é uma pipeline de ETL (Extract, Transform, Load) desenvolvida em Python utilizando **Pandas** e **Pathlib**. O objetivo é simular um fluxo básico de processamento de dados, desde a leitura de arquivos até a transformação e exportação dos dados tratados.

Tecnologias utilizadas

* Python 3.x
* Pandas
* Pathlib (biblioteca padrão do Python)

Estrutura do projeto

```
project/
│
├── data/
│   ├── raw/          # Dados brutos de entrada
│   └── processed/    # Dados após tratamento
│
├── src/
│   ├── extract.py    # Extração dos dados
│   ├── transform.py  # Transformação dos dados
│   └── load.py       # Salvamento dos dados processados
│
├── main.py           # Orquestração da pipeline
├── requirements.txt  # Dependências do projeto
└── README.md
```


Como funciona a pipeline

1. Extract (Extração)

Leitura dos arquivos localizados na pasta `data/raw/` utilizando Pandas.

2. Transform (Transformação)

Limpeza e manipulação dos dados, como:

* Remoção de valores nulos
* Padronização de colunas
* Conversão de tipos de dados

3. Load (Carga)

Exportação dos dados tratados para a pasta `data/processed/`.


Instalação

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```

Ative o ambiente:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Como executar

Execute o arquivo principal:

```bash
python main.py
```

---

Objetivo do projeto

Projeto desenvolvido para estudos e portfólio em engenharia/análise de dados, praticando conceitos de:

* Engenharia de dados básica
* Manipulação de dados com Pandas
* Organização de projetos em Python
* Estruturação de pipelines ETL



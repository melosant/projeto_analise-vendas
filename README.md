# ETL Análise de Vendas - dos Dados Sujos à Visualização de Insights

![Python](https://img.shields.io/badge/Python-3.14%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458)
![Status](https://img.shields.io/badge/Jupyter-orange)
![Status](https://img.shields.io/badge/Status-Finalizado-green)

## Sobre o Projeto
Este projeto simula um ambiente corporativo real de análise de dados. Dataset criado e sujado por IA.

O objetivo foi criar um pipeline que consome dados brutos e inconsistentes, realiza o tratamento e limpeza, modela as tabelas e gera visualizações estratégicas para tomada de decisão.

## Estrutura do Projeto

O projeto está dividido em etapas lógicas:

1. [**Criação do Database e tabelas com SQLite e SQLAlchemy**](src/config/database_models.py)

2. [**Processamento para análise de Insights**](src/pipelines)
    - [**ETL dos dados usando Pandas**](src/pipelines/processing.py)
    - [**Qualidade dos Dados**](src/pipelines/data_quality.py)

3. [**Insights com Jupyter**](src/notebooks/)

## Tecnologias Utilizadas
* **Python** (Linguagem Core)
* **Pandas** (Manipulação e Limpeza de Dados)
* **Plotly** (Visualização de Dados)
* **Jupyter Notebook** (Visualização de Insights)
* **SQLite** (SGBD)
* **SQLAlchemy** (Conexão com SGBD)
* **Git** (Controle de Versão)

# Data Warehouse de Vendas com Python e PostgreSQL


## 📘 Descrição do Projeto
Este projeto tem como objetivo a construção de um Data Warehouse (DW) simplificado para o domínio de vendas, utilizando Python e PostgreSQL.
O foco principal foi aplicar conceitos de engenharia de dados, como ETL (Extração, Transformação e Carga) e modelagem dimensional, sem uso de ferramentas de orquestração ou BI — apenas o ecossistema Python.

| Categoria                   | Ferramentas / Tecnologias            |
| --------------------------- | ------------------------------------ |
| Linguagem de programação    | Python                               |
| Bibliotecas principais      | pandas, sqlalchemy, psycopg2, dotenv |
| Banco de dados              | PostgreSQL                           |
| Modelagem de dados          | Esquema em estrela (Star Schema)     |
| Ambiente de desenvolvimento | Jupyter Notebook (.ipynb)            |


## ⚙️ Estrutura do Projeto

#### O projeto foi dividido em três etapas principais:

- Staging (Camada de Preparação)
- Extração dos dados brutos e tratamento inicial.

#### Arquivos principais:

- stg_pedidos.ipynb

- stg_vendedores.ipynb

#### Modelagem Dimensional

![banner](https://github.com/DanielPedroSantos/SuperStorePY/blob/main/Captura%20de%20tela%20de%202025-10-17%2018-55-28.png)


##### Criação das tabelas dimensionais e da tabela fato:

- dim_cliente_scd1

- dim_vendedores_scd1

- dim_produto_scd2

- dim_calendario

- fato_vendas

## Carga no Data Warehouse
Utilização do SQLAlchemy e Pandas para realizar a carga dos dados tratados no PostgreSQL, 
garantindo integridade referencial entre chaves substitutas (sk_) e chaves de negócio (id_).

## Conceitos Aplicados

ETL com Python puro (sem Apache Hop ou Airflow)

Uso de staging tables para controle de versões e qualidade dos dados

Modelagem dimensional com foco em performance analítica

Criação de surrogate keys (sk_)

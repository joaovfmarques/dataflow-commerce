# 🛒 DataFlow Commerce — Protótipo de Ciclo de Vida de Engenharia de Dados

**Disciplina:** Engenharia de Dados — CEUB
**Avaliação:** 1ª Avaliação (Menção Parcial 1) — Parte 1: Planejamento e Arquitetura
**Autor:** João Victor Ferreira Marques
**Matrícula:** 22303180
**Turma:** UN-0226 — Asa Norte — Matutino
**Data:** Abril/2026

---

## 📌 Sobre o Projeto

O **DataFlow Commerce** é um projeto de engenharia de dados aplicado ao cenário de uma plataforma de e-commerce de médio porte. O objetivo é planejar e documentar o ciclo de vida completo dos dados — desde a ingestão até o consumo — aplicando os princípios e arquiteturas estudados em aula.

Este repositório contém o planejamento arquitetural da **Parte 1** do projeto. A implementação prática será desenvolvida na Parte 2.

---

## 📂 Documentação

| Seção | Descrição |
|---|---|
| [01 - Descrição do Projeto](docs/01-descricao-projeto.md) | Contexto, problema e stakeholders |
| [02 - Dados](docs/02-dados.md) | Fontes, formatos, classificação e volume |
| [03 - Domínios e Serviços](docs/03-dominios-servicos.md) | Domínios de negócio e diagrama |
| [04 - Arquitetura](docs/04-arquitetura.md) | Fluxo de dados e decisões arquiteturais |
| [05 - Tecnologias](docs/05-tecnologias.md) | Stack técnica justificada |
| [06 - Considerações Finais](docs/06-consideracoes-finais.md) | Riscos, próximos passos e referências |

---

## 🧪 Provas de Conceito (PoCs)

Conforme orientação do tópico 8 do enunciado ("é importante fazer pequenas provas de conceito para validarem e justificar a escolha das tecnologias"), a pasta [`pocs/`](pocs/) contém experimentos mínimos que validam as principais escolhas tecnológicas da Parte 1:

| PoC | Tecnologia validada |
|---|---|
| [`pocs/docker-compose.yml`](pocs/docker-compose.yml) | Infraestrutura local integrada (Kafka, MinIO, Spark, Airflow, Superset) |
| [`pocs/kafka-producer/`](pocs/kafka-producer/) | Ingestão streaming com Apache Kafka |
| [`pocs/delta-lake/`](pocs/delta-lake/) | Armazenamento Lakehouse (MinIO + Delta Lake) |
| [`pocs/dbt/`](pocs/dbt/) | Modelagem analítica Silver → Gold com dbt |
| [`pocs/great-expectations/`](pocs/great-expectations/) | Qualidade de dados com Great Expectations |
| [`pocs/airflow/`](pocs/airflow/) | Orquestração de pipeline com Apache Airflow |

Detalhes de execução e evidências estão no [`pocs/README.md`](pocs/README.md).

---

## 🗂️ Estrutura do Repositório

```
dataflow-commerce/
├── README.md
├── docs/
│   ├── 01-descricao-projeto.md
│   ├── 02-dados.md
│   ├── 03-dominios-servicos.md
│   ├── 04-arquitetura.md
│   ├── 05-tecnologias.md
│   └── 06-consideracoes-finais.md
└── pocs/
    ├── README.md
    ├── docker-compose.yml
    ├── data/
    │   └── sample_pedidos.csv
    ├── kafka-producer/
    │   └── producer_clickstream.py
    ├── delta-lake/
    │   └── write_delta_minio.py
    ├── dbt/
    │   ├── dbt_project.yml
    │   └── models/
    │       └── stg_pedidos.sql
    ├── great-expectations/
    │   └── expectations_pedidos.py
    └── airflow/
        └── dags/
            └── pipeline_bronze_silver_gold.py
```

---

## 🧰 Stack Tecnológica (Resumo)

| Etapa | Tecnologia |
|---|---|
| Ingestão Streaming | Apache Kafka + Debezium |
| Ingestão Batch | Apache NiFi |
| Armazenamento | MinIO + Delta Lake |
| Processamento | Apache Spark + Spark Structured Streaming |
| Modelagem | dbt (dbt-spark) |
| Orquestração | Apache Airflow |
| Visualização | Apache Superset |
| Qualidade | Great Expectations |
| Governança | Apache Atlas |
| Monitoramento | Prometheus + Grafana |

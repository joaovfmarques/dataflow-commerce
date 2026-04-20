# 🛒 DataFlow Commerce — Protótipo de Ciclo de Vida de Engenharia de Dados

> **Disciplina:** Engenharia de Dados — CEUB
> > **Avaliação:** 1ª Avaliação (Menção Parcial 1) — Parte 1: Planejamento e Arquitetura
> > > **Autor:** João Vítor F. Marques
> > > > **Turma:** UN-0226 — Asa Norte — Matutino
> > > > > **Data:** Abril/2026
> > > > >
> > > > > ---
> > > > >
> > > > > ## 📌 Sobre o Projeto
> > > > >
> > > > > O **DataFlow Commerce** é um projeto de engenharia de dados aplicado ao cenário de uma plataforma de e-commerce de médio porte. O objetivo é planejar e documentar o ciclo de vida completo dos dados — desde a ingestão até o consumo — aplicando os princípios e arquiteturas estudados em aula.
> > > > >
> > > > > Este repositório contém o planejamento arquitetural da **Parte 1** do projeto. A implementação prática será desenvolvida na Parte 2.
> > > > >
> > > > > ---
> > > > >
> > > > > ## 📂 Documentação
> > > > >
> > > > > | Seção | Descrição |
> > > > > |---|---|
> > > > > | [01 - Descrição do Projeto](docs/01-descricao-projeto.md) | Contexto, problema e stakeholders |
> > > > > | [02 - Dados](docs/02-dados.md) | Fontes, formatos, classificação e volume |
> > > > > | [03 - Domínios e Serviços](docs/03-dominios-servicos.md) | Domínios de negócio e diagrama |
> > > > > | [04 - Arquitetura](docs/04-arquitetura.md) | Fluxo de dados e decisões arquiteturais |
> > > > > | [05 - Tecnologias](docs/05-tecnologias.md) | Stack técnica justificada |
> > > > > | [06 - Considerações Finais](docs/06-consideracoes-finais.md) | Riscos, próximos passos e referências |
> > > > >
> > > > > ---
> > > > >
> > > > > ## 🗂️ Estrutura do Repositório
> > > > >
> > > > > ```
> > > > > dataflow-commerce/
> > > > > ├── README.md
> > > > > └── docs/
> > > > >     ├── 01-descricao-projeto.md
> > > > >     ├── 02-dados.md
> > > > >     ├── 03-dominios-servicos.md
> > > > >     ├── 04-arquitetura.md
> > > > >     ├── 05-tecnologias.md
> > > > >     └── 06-consideracoes-finais.md
> > > > > ```
> > > > >
> > > > > ---
> > > > >
> > > > > ## 🧰 Stack Tecnológica (Resumo)
> > > > >
> > > > > | Etapa | Tecnologia |
> > > > > |---|---|
> > > > > | Ingestão Streaming | Apache Kafka + Debezium |
> > > > > | Ingestão Batch | Apache NiFi |
> > > > > | Armazenamento | MinIO + Delta Lake |
> > > > > | Processamento | Apache Spark + Spark Structured Streaming |
> > > > > | Modelagem | dbt (dbt-spark) |
> > > > > | Orquestração | Apache Airflow |
> > > > > | Visualização | Apache Superset |
> > > > > | Qualidade | Great Expectations |
> > > > > | Governança | Apache Atlas |
> > > > > | Monitoramento | Prometheus + Grafana |

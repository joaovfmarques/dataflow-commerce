# 5. Tecnologias — Como Será Feito

Todas as tecnologias escolhidas são **open-source e gratuitas**, podendo rodar localmente via Docker.

---

## 5.1 Ingestão

### Apache Kafka
**O que é:** Plataforma de streaming distribuído baseada em log de eventos.
**Por que foi escolhido:** É o padrão de mercado para ingestão de dados em tempo real. Garante alta throughput, tolerância a falhas (replicação), persistência das mensagens e desacoplamento entre produtores e consumidores. Os eventos de clickstream (~500/seg no pico) e de estoque são publicados em tópicos Kafka organizados por domínio (vendas.pedidos, comportamento.eventos, estoque.atualizacoes).
**Como se integra:** O Kafka atua como barramento central: o frontend publica eventos via Kafka Producer, e o Spark Structured Streaming os consome em tempo real.

### Apache NiFi + Debezium (CDC)
**O que é:** NiFi é uma ferramenta de integração de dados com interface visual; Debezium é um conector de Change Data Capture (CDC) para bancos relacionais.
**Por que foi escolhido:** Para dados batch (ERP, CRM, PostgreSQL), precisamos de extração agendada e CDC — captura de mudanças no banco sem queries full scan. O NiFi oferece isso com conectores prontos, sem código.
**Como se integra:** O NiFi lê as tabelas do PostgreSQL via Debezium e escreve os arquivos no Delta Lake (camada Bronze) no formato Avro/Parquet.

---

## 5.2 Armazenamento

### MinIO (Object Storage)
**O que é:** Sistema de armazenamento de objetos open-source, 100% compatível com a API do Amazon S3.
**Por que foi escolhido:** Permite rodar um storage escalável localmente ou em qualquer servidor, sem dependência de nuvem paga. É o "S3 local" — todas as ferramentas que se integram com S3 funcionam com MinIO sem mudança de código.
**Como se integra:** Armazena todos os arquivos do Lakehouse (camadas Bronze, Silver e Gold) em buckets organizados por domínio e por data de partição.

### Delta Lake
**O que é:** Camada de armazenamento open-source que adiciona suporte a ACID, schema enforcement, time travel e otimizações de leitura sobre arquivos Parquet no object storage.
**Por que foi escolhido:** Transforma o MinIO em um verdadeiro Lakehouse. Sem o Delta Lake, teríamos apenas um Data Lake sem garantias de consistência. Com ele, conseguimos fazer upserts, rollback de dados incorretos (time travel) e consultas analíticas com performance comparável a um Data Warehouse.
**Como se integra:** O Spark escreve e lê as tabelas Delta diretamente no MinIO. O dbt também se integra ao Delta Lake via Spark.

---

## 5.3 Processamento e Transformação

### Apache Spark
**O que é:** Motor de processamento distribuído para grandes volumes de dados, suportando batch e streaming.
**Por que foi escolhido:** É o padrão de mercado para processamento em escala. Suporta tanto processamento batch quanto streaming (via Spark Structured Streaming, consumindo tópicos Kafka em tempo real). Tem integração nativa com Delta Lake.
**Como se integra:** Os jobs de Spark são agendados pelo Airflow (batch) ou rodam continuamente (streaming). Escrevem os resultados nas camadas Silver e Gold do Lakehouse.

### dbt (Data Build Tool)
**O que é:** Ferramenta de transformação de dados que usa SQL para modelar e documentar tabelas analíticas.
**Por que foi escolhido:** Após o Spark limpar e padronizar os dados (Silver), o dbt cria os modelos analíticos da camada Gold — tabelas de fatos e dimensões (modelo estrela), métricas de negócio e agregações. O dbt gera documentação automática e testa a qualidade dos dados com assertions SQL.
**Como se integra:** Roda sobre o Spark (via dbt-spark adapter), lê da Silver e escreve na Gold. Integrado ao Airflow para execução agendada.

---

## 5.4 Orquestração

### Apache Airflow
**O que é:** Plataforma de orquestração de workflows baseada em DAGs (Directed Acyclic Graphs).
**Por que foi escolhido:** Permite agendar e monitorar pipelines de dados, definir dependências entre tarefas, monitorar falhas, reprocessar partições específicas e ter visibilidade completa de todos os pipelines em uma interface web.
**Como se integra:** Orquestra todos os jobs batch: extração via NiFi, processamento via Spark, modelagem via dbt. Os pipelines de streaming (Kafka + Spark Streaming) rodam de forma contínua independente.

---

## 5.5 Consumo

### Apache Superset
**O que é:** Ferramenta open-source de Business Intelligence (BI) e visualização de dados.
**Por que foi escolhido:** Permite criar dashboards interativos conectando diretamente às tabelas Gold do Lakehouse via SQL. É gratuito, fácil de usar e suporta gráficos, filtros e alertas.
**Como se integra:** Conecta ao Spark SQL para consultar as tabelas da camada Gold.

### Jupyter Notebooks
**O que é:** Ambiente interativo para análise exploratória de dados e desenvolvimento de modelos de ML.
**Por que foi escolhido:** Os cientistas de dados precisam de acesso flexível para construir modelos de recomendação e previsão de demanda.
**Como se integra:** Conecta ao Spark cluster e ao MinIO diretamente.

---

## 5.6 Correntes do Ciclo de Vida (Transversais)

### Great Expectations — Qualidade de Dados
**O que é:** Framework open-source para validação e testes de qualidade de dados.
**Por que foi escolhido:** Garante que os dados na camada Silver atendam a regras de negócio (ex.: valor do pedido não pode ser negativo; id_cliente não pode ser nulo). Gera relatórios de qualidade automaticamente.
**Como se integra:** Roda como uma etapa dos DAGs do Airflow após o processamento do Spark.

### Apache Atlas — Governança e Linhagem
**O que é:** Plataforma open-source de governança de dados, catálogo e rastreamento de linhagem.
**Por que foi escolhido:** Permite saber de onde cada dado veio, quem o transformou e onde ele foi usado (data lineage). Essencial para conformidade e resolução de problemas de qualidade.
**Como se integra:** Captura metadados automaticamente do Spark e do Kafka via hooks de integração.

### Prometheus + Grafana — Monitoramento
**O que é:** Prometheus coleta métricas de sistemas; Grafana as visualiza em dashboards.
**Por que foi escolhido:** Monitora a saúde de todos os componentes: lag do Kafka, duração dos jobs Spark, taxa de falhas do Airflow, uso de disco no MinIO. Gera alertas quando algo sai do normal.
**Como se integra:** Cada componente expõe métricas via endpoint Prometheus; o Grafana exibe dashboards em tempo real.

---

## 5.7 Resumo da Stack

| Etapa | Tecnologia | Tipo |
|---|---|---|
| Ingestão streaming | Apache Kafka | Open-source |
| Ingestão batch / CDC | Apache NiFi + Debezium | Open-source |
| Armazenamento | MinIO + Delta Lake | Open-source |
| Processamento batch | Apache Spark | Open-source |
| Processamento streaming | Spark Structured Streaming | Open-source |
| Transformação / Modelagem | dbt (dbt-spark) | Open-source |
| Orquestração | Apache Airflow | Open-source |
| Visualização / BI | Apache Superset | Open-source |
| Análise / ML | Jupyter Notebooks + PySpark | Open-source |
| Qualidade de Dados | Great Expectations | Open-source |
| Governança / Linhagem | Apache Atlas | Open-source |
| Monitoramento | Prometheus + Grafana | Open-source |

# 🧪 Provas de Conceito — DataFlow Commerce

Esta pasta contém as **provas de conceito (PoCs)** citadas no tópico 8 do enunciado da 1ª Avaliação. O objetivo não é implementar o projeto completo (isso é a Parte 2), mas sim **validar e justificar, com pequenos experimentos, as principais escolhas tecnológicas** documentadas na Parte 1.

## Mapeamento PoC ↔ Decisão de Arquitetura

| PoC | Decisão validada (ver `docs/05-tecnologias.md`) |
|---|---|
| `docker-compose.yml` | Todos os serviços open-source sobem localmente de forma integrada, validando a viabilidade da stack. |
| `kafka-producer/producer_clickstream.py` | Kafka consegue receber eventos JSON de clickstream com o mesmo schema descrito em `docs/02-dados.md`. |
| `delta-lake/write_delta_minio.py` | MinIO + Delta Lake funcionam como Lakehouse: leitura de CSV, escrita em tabela Delta com ACID e schema enforcement. |
| `dbt/` | dbt consegue modelar uma tabela Silver a partir dos dados Bronze, materializando a camada Gold. |
| `great-expectations/expectations_pedidos.py` | Great Expectations valida regras de negócio sobre a tabela de pedidos (`valor > 0`, `id_cliente não nulo`). |
| `airflow/dags/pipeline_bronze_silver_gold.py` | Airflow orquestra um DAG com as três etapas Bronze → Silver → Gold e dependências entre tarefas. |

## Como executar (Parte 2)

Os PoCs abaixo são **esqueletos mínimos**. Na Parte 2 do projeto, serão expandidos para o pipeline completo. Por enquanto, servem como evidência de que cada tecnologia escolhida é viável e se integra com as demais.

```bash
# Subir a infraestrutura local
docker compose -f pocs/docker-compose.yml up -d

# Gerar eventos de clickstream no Kafka
python pocs/kafka-producer/producer_clickstream.py

# Escrever um CSV de pedidos como tabela Delta no MinIO
spark-submit pocs/delta-lake/write_delta_minio.py

# Rodar o modelo dbt (Silver -> Gold)
cd pocs/dbt && dbt run --select stg_pedidos

# Validar qualidade dos pedidos
python pocs/great-expectations/expectations_pedidos.py
```

## Dados de exemplo

O arquivo `data/sample_pedidos.csv` contém um pequeno conjunto de pedidos fictícios usado por todos os PoCs que precisam de dados tabulares.

## Observação

Conforme o tópico 8 do enunciado: *"Não é necessário implementar nada nesta parte. O foco é o planejamento arquitetural. Mas é importante fazer pequenas provas de conceito para validarem e justificar a escolha das tecnologias."* Os experimentos aqui atendem exatamente a essa orientação.

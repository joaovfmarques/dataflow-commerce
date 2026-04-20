"""
PoC — DAG Airflow: pipeline Bronze -> Silver -> Gold
====================================================

Objetivo
--------
Validar a escolha do Apache Airflow como orquestrador, conforme
`docs/05-tecnologias.md` (secao 5.4).

Esta DAG e um esqueleto minimo que materializa a arquitetura Medallion
descrita em `docs/04-arquitetura.md` (secao 4.2). Ela encadeia:

  ingest_bronze  -> transform_silver  -> validate_quality  -> build_gold

As tasks sao PythonOperators que apenas imprimem o que fariam, para
comprovar que a orquestracao funciona e as dependencias estao corretas.
Na Parte 2, cada task sera substituida pela chamada real ao NiFi, Spark,
Great Expectations e dbt.

Uso
---
  docker compose -f pocs/docker-compose.yml up -d airflow
  # Acesse http://localhost:8082, login airflow/airflow
"""

from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "dataflow-commerce",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def ingest_bronze(**_: object) -> None:
    print("[Bronze] NiFi + Debezium extraindo dados brutos para o Delta Lake...")


def transform_silver(**_: object) -> None:
    print("[Silver] Spark limpando, tipando e deduplicando dados Bronze...")


def validate_quality(**_: object) -> None:
    print("[Quality] Great Expectations validando regras de negocio na Silver...")


def build_gold(**_: object) -> None:
    print("[Gold] dbt construindo tabelas fato e dimensao na camada Gold...")


with DAG(
    dag_id="pipeline_bronze_silver_gold",
    description="PoC do pipeline Medallion do DataFlow Commerce",
    default_args=default_args,
    start_date=datetime(2026, 4, 1),
    schedule_interval="0 2 * * *",
    catchup=False,
    tags=["dataflow-commerce", "poc", "medallion"],
) as dag:

    t1 = PythonOperator(
        task_id="ingest_bronze",
        python_callable=ingest_bronze,
    )

    t2 = PythonOperator(
        task_id="transform_silver",
        python_callable=transform_silver,
    )

    t3 = PythonOperator(
        task_id="validate_quality",
        python_callable=validate_quality,
    )

    t4 = PythonOperator(
        task_id="build_gold",
        python_callable=build_gold,
    )

    t1 >> t2 >> t3 >> t4

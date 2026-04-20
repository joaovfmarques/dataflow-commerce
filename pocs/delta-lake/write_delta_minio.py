"""
PoC — Escrever uma tabela Delta Lake no MinIO via PySpark
=========================================================

Objetivo
--------
Validar a escolha do Lakehouse (MinIO + Delta Lake) como camada de
armazenamento, conforme documentado em `docs/04-arquitetura.md` (secao 4.1)
e `docs/05-tecnologias.md` (secao 5.2).

O script le o CSV `pocs/data/sample_pedidos.csv` (camada Bronze simulada)
e escreve-o como tabela Delta em `s3a://bronze/pedidos` no MinIO.
Depois executa uma consulta simples para comprovar a leitura.

Pre-requisitos
--------------
  docker compose -f pocs/docker-compose.yml up -d minio spark-master spark-worker
  pip install pyspark==3.5.0 delta-spark==3.1.0

Uso
---
  spark-submit --packages io.delta:delta-spark_2.12:3.1.0,org.apache.hadoop:hadoop-aws:3.3.4 \\
    pocs/delta-lake/write_delta_minio.py
"""

from pyspark.sql import SparkSession


MINIO_ENDPOINT = "http://localhost:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"

CSV_PATH = "pocs/data/sample_pedidos.csv"
DELTA_PATH = "s3a://bronze/pedidos"


def build_spark() -> SparkSession:
    return (
        SparkSession.builder
        .appName("poc-delta-minio")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        .config("spark.hadoop.fs.s3a.endpoint", MINIO_ENDPOINT)
        .config("spark.hadoop.fs.s3a.access.key", MINIO_ACCESS_KEY)
        .config("spark.hadoop.fs.s3a.secret.key", MINIO_SECRET_KEY)
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem",
        )
        .getOrCreate()
    )


def main() -> None:
    spark = build_spark()

    print(f"Lendo CSV de exemplo: {CSV_PATH}")
    df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(CSV_PATH)
    )
    df.printSchema()
    df.show(truncate=False)

    print(f"Escrevendo como tabela Delta em: {DELTA_PATH}")
    (
        df.write
        .format("delta")
        .mode("overwrite")
        .save(DELTA_PATH)
    )

    print("Lendo a tabela Delta de volta para validar ACID + schema:")
    back = spark.read.format("delta").load(DELTA_PATH)
    back.groupBy("status").count().show()

    spark.stop()
    print("PoC concluida. Verifique no MinIO Console: http://localhost:9001")


if __name__ == "__main__":
    main()

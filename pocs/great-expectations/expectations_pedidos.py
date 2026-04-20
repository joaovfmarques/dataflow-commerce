"""
PoC - Great Expectations sobre a tabela de pedidos
==================================================

Objetivo
--------
Validar a escolha do Great Expectations como ferramenta de qualidade de
dados, conforme documentado em docs/05-tecnologias.md (secao 5.6).

Este script carrega pocs/data/sample_pedidos.csv em um DataFrame pandas
e aplica um conjunto minimo de expectativas sobre a tabela Silver de
pedidos. As expectativas validam regras de negocio chave:

  1. id_pedido e unico e nao nulo
  2. id_cliente nao e nulo
  3. valor e sempre maior que zero
  4. status so pode assumir valores conhecidos
  5. quantidade e um inteiro positivo

Uso
---
  pip install great_expectations pandas
  python pocs/great-expectations/expectations_pedidos.py
"""

import pandas as pd
import great_expectations as gx

CSV_PATH = "pocs/data/sample_pedidos.csv"
ALLOWED_STATUS = ["pago", "pendente", "cancelado"]


def main() -> None:
    df = pd.read_csv(CSV_PATH)

    context = gx.get_context()
    datasource = context.sources.add_pandas(name="poc_pedidos_ds")
    asset = datasource.add_dataframe_asset(name="pedidos")

    validator = context.get_validator(
        batch_request=asset.build_batch_request(dataframe=df),
        expectation_suite_name="pedidos_silver_v1",
    )

    # 1. id_pedido unico e nao nulo
    validator.expect_column_values_to_not_be_null("id_pedido")
    validator.expect_column_values_to_be_unique("id_pedido")

    # 2. id_cliente nao nulo
    validator.expect_column_values_to_not_be_null("id_cliente")

    # 3. valor > 0
    validator.expect_column_values_to_be_between(
        "valor", min_value=0.01, strict_min=True
    )

    # 4. status dentro do dominio
    validator.expect_column_values_to_be_in_set("status", ALLOWED_STATUS)

    # 5. quantidade inteiro positivo
    validator.expect_column_values_to_be_between(
        "quantidade", min_value=1, strict_min=False
    )

    result = validator.validate()
    print("Sucesso?", result.success)
    for r in result.results:
        ok = "OK" if r.success else "FALHA"
        print(f"  [{ok}] {r.expectation_config.expectation_type}")

    validator.save_expectation_suite(discard_failed_expectations=False)


if __name__ == "__main__":
    main()

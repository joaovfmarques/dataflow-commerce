-- PoC dbt: modelo de staging para pedidos (camada Silver)
-- Le os dados brutos (Bronze) e produz uma versao limpa, tipada e validada.
-- Valida a escolha do dbt para modelagem analitica (ver docs/05-tecnologias.md secao 5.3).

{{ config(materialized='view', schema='silver') }}

with raw as (
    select *
    from {{ source('bronze', 'pedidos') }}
),

cleaned as (
    select
        cast(id_pedido   as bigint)   as id_pedido,
        cast(id_cliente  as bigint)   as id_cliente,
        cast(id_produto  as string)   as id_produto,
        cast(quantidade  as int)      as quantidade,
        cast(valor       as decimal(10,2)) as valor,
        cast(data        as date)     as data_pedido,
        lower(trim(status))           as status,
        lower(trim(forma_pagamento))  as forma_pagamento
    from raw
    where id_pedido is not null
      and valor > 0
)

select * from cleaned

# 6. Considerações Finais

## 6.1 Principais Riscos e Limitações

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Complexidade de infraestrutura local (Docker) | Alta | Médio | Usar Docker Compose com configurações pré-definidas para subir todos os serviços com um único comando |
| Volume de dados de pico (Black Friday) sobrecarregar o Kafka | Média | Alto | Configurar particionamento adequado nos tópicos e escalonamento horizontal dos consumers |
| Schema evolution (mudança no formato dos dados) | Média | Alto | Usar Schema Registry do Kafka para controlar versões de schemas e evitar quebra de compatibilidade |
| Qualidade dos dados no sistema de origem (dados sujos) | Alta | Alto | Implementar validações com Great Expectations na camada Silver e criar alertas para dados fora do padrão |
| Limitações de hardware local para rodar Spark + Kafka + MinIO | Alta | Médio | Dimensionar jobs Spark com modo local (não distribuído) na Parte 2; otimizar uso de memória |
| Curva de aprendizado das ferramentas | Média | Baixo | Utilizar documentação oficial e imagens Docker pré-configuradas da comunidade |

---

## 6.2 Próximos Passos para a Parte 2 (Implementação)

A Parte 2 do projeto consiste na implementação prática do que foi planejado aqui. As etapas previstas são:

1. **Configurar o ambiente local** com Docker Compose contendo: Kafka, Zookeeper, NiFi, MinIO, Spark, Airflow, Superset e Great Expectations.
2. **Criar os tópicos Kafka** para os domínios: vendas.pedidos, comportamento.clickstream, estoque.atualizacoes.
3. **Implementar o produtor de dados simulados** (script Python) para gerar eventos de teste realistas.
4. **Configurar o pipeline NiFi** para extração batch do banco PostgreSQL.
5. **Desenvolver os jobs Spark** para transformação Bronze → Silver (limpeza, tipagem, deduplicação).
6. **Criar os modelos dbt** para transformação Silver → Gold (tabelas fato_pedidos, dim_clientes, dim_produtos).
7. **Construir os DAGs do Airflow** para orquestrar o pipeline batch completo.
8. **Criar os dashboards no Superset** conectados à camada Gold.
9. **Implementar testes de qualidade** com Great Expectations nas camadas Silver e Gold.

---

## 6.3 Referências

- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. O'Reilly Media, 2017.
- REIS, Joe; HOUSLEY, Matt. *Fundamentals of Data Engineering*. O'Reilly Media, 2022.
- ARMBRUST, Michael et al. *Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics*. CIDR, 2021.
- Apache Kafka Documentation. Disponível em: https://kafka.apache.org/documentation/
- Delta Lake Documentation. Disponível em: https://docs.delta.io/
- Apache Airflow Documentation. Disponível em: https://airflow.apache.org/docs/
- dbt Documentation. Disponível em: https://docs.getdbt.com/
- Apache Spark Documentation. Disponível em: https://spark.apache.org/docs/latest/
- Great Expectations Documentation. Disponível em: https://docs.greatexpectations.io/
- Apache Atlas Documentation. Disponível em: https://atlas.apache.org/

# 1. Descrição do Projeto

## 1.1 Nome e Contexto de Negócio

**Nome do Projeto:** DataFlow Commerce

**Cenário:** Plataforma de e-commerce de médio porte com catálogo de ~50.000 produtos, operando em todo o Brasil, com aproximadamente 200.000 usuários ativos por mês e pico de acessos em datas comemorativas (Black Friday, Natal).

A empresa processa pedidos, gerencia estoque, realiza campanhas de marketing digital e precisa monitorar a experiência do usuário em tempo real no site e no aplicativo mobile.

## 1.2 Problema que o Projeto Pretende Resolver

A empresa enfrenta os seguintes desafios:

- **Falta de visibilidade em tempo real:** a equipe de negócio não sabe quantos carrinhos estão sendo abandonados agora, nem quais produtos estão em falta no estoque neste momento.
- **Relatórios fragmentados:** os dados de vendas, marketing e logística estão em sistemas separados (banco transacional, planilhas, CRM), dificultando análises integradas.
- **Decisões baseadas em dados desatualizados:** os relatórios gerenciais são gerados manualmente, com atraso de até 24 horas.
- **Ausência de pipeline de dados estruturado:** não existe um processo confiável e automatizado de coleta, transformação e disponibilização dos dados para as equipes analíticas.

O projeto visa construir uma plataforma de dados unificada que integre todas as fontes, processe dados em batch e em streaming, e disponibilize informações confiáveis e atualizadas para tomada de decisão.

## 1.3 Objetivos Principais

- Centralizar todos os dados da empresa em uma arquitetura Lakehouse.
- Processar eventos de comportamento do usuário em tempo real (streaming).
- Gerar relatórios e dashboards automatizados e confiáveis (batch).
- Garantir qualidade, governança e rastreabilidade dos dados.

## 1.4 Principais Stakeholders e Usuários Finais dos Dados

| Stakeholder | Papel | Necessidade |
|---|---|---|
| Diretoria / C-Level | Decisores estratégicos | Dashboards executivos: receita, crescimento, CAC, LTV |
| Time de Marketing | Usuários analíticos | Análise de campanhas, taxa de conversão, comportamento do usuário |
| Time de Logística | Usuários operacionais | Status de pedidos, tempo de entrega, falhas na cadeia |
| Time de Estoque | Usuários operacionais | Alertas de ruptura de estoque, giro de produtos |
| Time de TI / Dados | Produtores e mantenedores | Pipelines, qualidade dos dados, monitoramento |
| Cientistas de Dados | Consumidores analíticos | Modelos de recomendação, previsão de demanda, churn |

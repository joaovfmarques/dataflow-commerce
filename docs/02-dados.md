# 2. Definição e Classificação dos Dados

## 2.1 Fontes de Dados

| Fonte | Sistema de Origem | Formato | Frequência | Latência Esperada |
|---|---|---|---|---|
| Pedidos e transações | Banco transacional (PostgreSQL) | Estruturado / Relacional | Contínuo | < 5 min (CDC) |
| Catálogo de produtos | ERP interno | JSON / CSV | Diário (batch) | 24h |
| Estoque | ERP interno | JSON | A cada atualização | < 1 min (streaming) |
| Cliques e navegação | Frontend (JavaScript) | JSON (eventos) | Tempo real | < 1 seg (streaming) |
| Carrinho abandonado | Frontend + Backend | JSON | Tempo real | < 5 seg (streaming) |
| Campanhas de marketing | CRM externo | CSV / API REST | Diário (batch) | 24h |
| Avaliações e reviews | Backend da plataforma | JSON | Batch noturno | 24h |
| Logs de aplicação | Servidores e containers | JSON estruturado | Contínuo | < 30 seg (streaming) |

## 2.2 Classificação dos Dados

### 2.2.1 Dados Operacionais (Batch)

- **Pedidos finalizados:** id_pedido, id_cliente, id_produto, quantidade, valor, data, status, forma de pagamento. Volume: ~5.000/dia.
- **Catálogo de produtos:** nome, descrição, categoria, preço, SKU. Volume: ~50.000 registros, atualização diária.
- **Dados de marketing:** campanhas, CPC, taxa de conversão. Volume: ~500 registros/dia.
- **Avaliações:** texto, nota (1-5), data, id_cliente. Volume: ~1.000/dia.

### 2.2.2 Dados de Streaming

- **Eventos de navegação:** page_view, product_view, add_to_cart, checkout_start. Volume: ~500 eventos/seg (pico).
- **Eventos de estoque:** stock_update. Volume: ~200 eventos/min.
- **Carrinho abandonado:** session abandonment events. Volume: ~50 eventos/min.
- **Logs de sistema:** erros, latência de API, falhas de pagamento. Volume: ~1.000 linhas/min.

## 2.3 Detalhes por Fonte

| Fonte | Formato | Volume | Periodicidade | Latência |
|---|---|---|---|---|
| Pedidos (CDC) | Avro / JSON | 5.000/dia | Contínuo | < 5 min |
| Catálogo | JSON | 50.000 registros | Diário | 24h |
| Eventos de navegação | JSON | 500 eventos/seg | Tempo real | < 1 seg |
| Estoque | JSON | 200 eventos/min | Tempo real | < 1 min |
| Marketing (CRM) | CSV | 500/dia | Diário | 24h |
| Avaliações | JSON | 1.000/dia | Noturno | 24h |
| Logs | JSON estruturado | 1.000 linhas/min | Contínuo | < 30 seg |

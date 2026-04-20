"""
PoC — Produtor de eventos de clickstream para Apache Kafka
==========================================================

Objetivo
--------
Validar a escolha do Apache Kafka como camada de ingestao streaming,
conforme documentado em `docs/05-tecnologias.md` (secao 5.1).

Este script publica eventos JSON de clickstream no topico
`comportamento.clickstream`, simulando o comportamento real de usuarios
no site/app do e-commerce (ver volumes em `docs/02-dados.md`).

Pre-requisitos
--------------
  pip install kafka-python

  docker compose -f pocs/docker-compose.yml up -d kafka

Uso
---
  python pocs/kafka-producer/producer_clickstream.py
"""

import json
import random
import time
import uuid
from datetime import datetime

from kafka import KafkaProducer

KAFKA_BOOTSTRAP = "localhost:9092"
TOPIC = "comportamento.clickstream"

EVENT_TYPES = [
    "page_view",
    "product_view",
    "add_to_cart",
    "checkout_start",
    "checkout_complete",
]

PRODUCT_IDS = [f"SKU-{i:05d}" for i in range(1, 101)]


def build_event() -> dict:
    """Gera um evento de clickstream fake com o schema descrito em docs/02-dados.md."""
    return {
        "event_id": str(uuid.uuid4()),
        "event_type": random.choice(EVENT_TYPES),
        "user_id": f"user-{random.randint(1, 10_000)}",
        "session_id": str(uuid.uuid4()),
        "product_id": random.choice(PRODUCT_IDS),
        "url": f"/produto/{random.choice(PRODUCT_IDS).lower()}",
        "referrer": random.choice(["google", "direct", "instagram", "email"]),
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


def main(num_events: int = 500, rate_per_sec: int = 50) -> None:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        acks="all",
        linger_ms=5,
    )

    print(f"Publicando {num_events} eventos em '{TOPIC}' a ~{rate_per_sec} ev/s...")
    for i in range(num_events):
        event = build_event()
        producer.send(TOPIC, value=event)
        if i % 50 == 0:
            print(f"  {i} eventos publicados | ultimo: {event['event_type']}")
        time.sleep(1 / rate_per_sec)

    producer.flush()
    producer.close()
    print("Concluido. Verifique em http://localhost:8080 (Kafka UI).")


if __name__ == "__main__":
    main()

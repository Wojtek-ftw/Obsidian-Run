# Firehose Processor with Redis and Docker

This project simulates a real-time streaming data pipeline using Redis pub/sub, where events are processed by multiple models with different latencies. It's fully Dockerized with separate services for publishing and processing.

---

## Project Structure

```
firehose_project/
├── README.md
├── Makefile
├── docker-compose.yml
├── processor/
│   ├── Dockerfile
│   ├── firehose_processor.py
│   ├── requirements.txt
│   └── output.csv        # Output generated here
├── publisher/
│   ├── Dockerfile
│   ├── firehose_publisher.py
│   └── requirements.txt
```

---

## Quick Start

### 1. Clone or unzip the project

```bash
cd firehose_project
```

### 2. Build the containers

```bash
make build
docker-compose build
```

### 3. Run the services

```bash
make up
docker-compose up
```

- `redis`: In-memory message broker
- `publisher`: Simulates a firehose by publishing events every 2–3ms
- `processor`: Subscribes to Redis, runs 3 models with different latencies, and saves results to `output.csv`

The publisher runs for 5 minutes.

### 4. View the output

```bash
cat processor/output.csv | head
```

### 5. Stop everything

```bash
make down
docker-compose down
```

---

## Simulated Model Latencies

| Model  | Latency |
|--------|---------|
| model1 | 3ms     |
| model2 | 250ms   |
| model3 | 1s      |

The processor decides which models to run for each incoming event using a dispatching strategy.

---

## Notes

- The `output.csv` includes the original event timestamp and the timestamps for when each model completed.
- The processor is written with `asyncio` to allow concurrent model execution.
- The firehose simulates high-frequency data ingestion as might be seen in trading platforms or telemetry systems.
- Events that aren't immediately processed by the model are dropped, ensuring there is at least one element available for processing.

---

## Requirements

- Docker
- Docker Compose

No local Python installation is required — everything runs in containers.

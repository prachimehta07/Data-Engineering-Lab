# Practical 3 – Real-Time Data Ingestion using Apache Kafka

## Overview

This practical demonstrates a simple real-time data ingestion pipeline using **Apache Kafka** and **Python**.

A Python producer continuously publishes simulated web application activity logs to a Kafka topic, while a Python consumer receives the events in real time and measures performance metrics such as **message latency** and **processing throughput**.

The implementation focuses on understanding the basic Producer → Broker → Consumer architecture used in modern event-driven systems.

---

## Objectives

- Configure Apache Kafka in KRaft mode.
- Create a Kafka topic.
- Implement a Kafka Producer using Python.
- Implement a Kafka Consumer using Python.
- Stream real-time web activity logs.
- Measure latency and throughput.

---

## Technologies Used

- Apache Kafka 3.9
- Python 3.x
- kafka-python-ng
- Pandas
- JSON

---

## Dataset

The producer generates simulated web application activity events.

Example:

```json
{
  "user_id":101,
  "action":"login",
  "page":"home"
}
```

Each message contains a timestamp used for latency calculation.

---

## Project Structure

```
practical-03-kafka-streaming/

│── producer.py

│── consumer.py

│── sample-output/

│ └── output.txt

│── screenshots/

│ ├── producer-consumer.png

│ └── performance-results.png

└── README.md
```

---

## Architecture

```
Python Producer

↓

Kafka Broker

↓

Topic (web_activity_logs)

↓

Python Consumer

↓

Latency & Throughput
```

---

## Running the Project

### Start Kafka Server

```bash
bin\windows\kafka-server-start.bat config\kraft\server.properties
```

### Create Topic

```bash
bin\windows\kafka-topics.bat --create --topic web_activity_logs --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### Start Consumer

```bash
python consumer.py
```

### Start Producer

```bash
python producer.py
```

---

## Performance Metrics

### Latency

Measures the time taken for a message to travel from Producer to Consumer.

```
Latency = Receive Time − Send Time
```

Measured in milliseconds (ms).

### Throughput

Measures how many messages are processed every second.

```
Throughput = Number of Messages / Total Processing Time
```

Measured in messages/second.

---

## Sample Output

A sample execution is available in:

```
sample-output/output.txt
```

---

## Screenshots

- Producer and Consumer Execution
- Performance Results

---

## Learning Outcomes

- Understand Kafka Producer and Consumer architecture.
- Learn how real-time event streaming works.
- Measure streaming latency.
- Measure throughput.
- Gain practical experience with Apache Kafka.

---

## Future Improvements

- Implement a micro-batch ingestion pipeline.
- Compare batch and streaming performance.
- Scale the Kafka topic using multiple partitions.
- Evaluate consumer groups under high load.
- Deploy Kafka using Docker containers.

---

## Author

Prachi Mehta
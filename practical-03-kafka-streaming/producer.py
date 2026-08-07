from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

topic = "web_activity_logs"

events = [
    {"user_id": 101, "action": "login", "page": "home"},
    {"user_id": 101, "action": "search", "page": "laptops"},
    {"user_id": 102, "action": "view_product", "page": "mobile"},
    {"user_id": 103, "action": "add_to_cart", "page": "cart"},
    {"user_id": 101, "action": "checkout", "page": "payment"},
    {"user_id": 104, "action": "login", "page": "home"},
    {"user_id": 105, "action": "search", "page": "headphones"},
    {"user_id": 102, "action": "logout", "page": "profile"},
    {"user_id": 106, "action": "login", "page": "home"},
    {"user_id": 107, "action": "view_product", "page": "electronics"}
]

print("Producer Started")

for event in events:

    event["timestamp"] = time.time()

    producer.send(topic, event)

    print("Sent :", event)

    time.sleep(1)

producer.flush()
producer.close()

print("Producer Finished")
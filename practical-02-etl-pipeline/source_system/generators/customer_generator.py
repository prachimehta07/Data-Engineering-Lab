import json
import random
from faker import Faker

fake = Faker()

def make_customer(customer_id):
    customer = {
        "customer_id": customer_id,
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.msisdn()[:10],
        "age": random.randint(18, 70)
    }
    return customer

def inject_errors(customers):
    # Now we pick some random customers and break them on purpose
    total = len(customers)

    # missing email
    for i in random.sample(range(total), 5):
        customers[i]["email"] = None

    # invalid email format
    for i in random.sample(range(total), 5):
        customers[i]["email"] = customers[i]["name"].replace(" ", "").lower() + "gmail.com"

    # missing phone
    for i in random.sample(range(total), 4):
        customers[i]["phone"] = ""

    # invalid phone (too short)
    for i in random.sample(range(total), 4):
        customers[i]["phone"] = "12345"

    # negative age
    for i in random.sample(range(total), 3):
        customers[i]["age"] = -5

    # age too high
    for i in random.sample(range(total), 3):
        customers[i]["age"] = 250

    # empty name
    for i in random.sample(range(total), 2):
        customers[i]["name"] = ""

    # duplicate customer id (copy id from another record)
    for i in random.sample(range(total), 3):
        copy_from = random.randint(0, total - 1)
        customers[i]["customer_id"] = customers[copy_from]["customer_id"]

    return customers

def generate_customers(count=100):
    customers = [make_customer(i + 1) for i in range(count)]
    customers = inject_errors(customers)
    return customers

if __name__ == "__main__":
    customers = generate_customers(100)

    with open("source_system/data/customers.json", "w") as f:
        json.dump(customers, f, indent=4)

    print(f"Generated {len(customers)} customers -> source_system/data/customers.json")
import json
import random
from faker import Faker

fake = Faker()

def make_transaction(transaction_id):
    txn = {
        "transaction_id": transaction_id,
        "customer": {"id": random.randint(1, 100)},
        "payment": {
            "amount": round(random.uniform(100, 20000), 2),
            "method": random.choice(["UPI", "CARD", "NETBANKING", "COD"])
        },
        "device": random.choice(["mobile", "desktop", "tablet"]),
        "date": fake.date_between(start_date="-30d", end_date="today").isoformat()
    }
    return txn

def inject_errors(transactions):
    total = len(transactions)

    # negative amount
    for i in random.sample(range(total), 4):
        transactions[i]["payment"]["amount"] = -transactions[i]["payment"]["amount"]

    # invalid payment method
    for i in random.sample(range(total), 4):
        transactions[i]["payment"]["method"] = "BitcoinCashUPI"

    # missing payment object entirely
    for i in random.sample(range(total), 3):
        transactions[i]["payment"] = None

    # missing customer id
    for i in random.sample(range(total), 3):
        transactions[i]["customer"]["id"] = None

    # wrong date format
    for i in random.sample(range(total), 3):
        transactions[i]["date"] = "15/06/2026"

    return transactions

def generate_transactions(count=100):
    transactions = [make_transaction(i + 1) for i in range(count)]
    transactions = inject_errors(transactions)
    return transactions

if __name__ == "__main__":
    transactions = generate_transactions(100)

    with open("source_system/data/transactions.json", "w") as f:
        json.dump(transactions, f, indent=4)

    print(f"Generated {len(transactions)} transactions -> source_system/data/transactions.json")
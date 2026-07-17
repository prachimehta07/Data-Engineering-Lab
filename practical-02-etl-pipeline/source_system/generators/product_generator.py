import sqlite3
import random
from faker import Faker

fake = Faker()

def make_product(product_id):
    product = {
        "product_id": product_id,
        "product_name": fake.word().capitalize() + " " + fake.word().capitalize(),
        "category": random.choice(["Electronics", "Grocery", "Clothing", "Furniture", "Toys"]),
        "price": round(random.uniform(50, 60000), 2)
    }
    return product

def inject_errors(products):
    total = len(products)

    # negative price
    for i in random.sample(range(total), 3):
        products[i]["price"] = -products[i]["price"]

    # null category
    for i in random.sample(range(total), 3):
        products[i]["category"] = None

    # duplicate product id
    for i in random.sample(range(total), 2):
        copy_from = random.randint(0, total - 1)
        products[i]["product_id"] = products[copy_from]["product_id"]

    return products

def generate_products(count=50):
    products = [make_product(i + 1) for i in range(count)]
    products = inject_errors(products)
    return products

if __name__ == "__main__":
    products = generate_products(50)

    conn = sqlite3.connect("source_system/database/products.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute("""
        CREATE TABLE products (
            product_id INTEGER,
            product_name TEXT,
            category TEXT,
            price REAL
        )
    """)

    for p in products:
        cursor.execute(
            "INSERT INTO products (product_id, product_name, category, price) VALUES (?, ?, ?, ?)",
            (p["product_id"], p["product_name"], p["category"], p["price"])
        )

    conn.commit()
    conn.close()

    print(f"Generated {len(products)} products -> source_system/database/products.db")
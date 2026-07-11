# Mock E-Commerce Schema

This is the mock schema referenced by the Generation stage of the architecture (`OLTP PostgreSQL` box). It represents a simplified transactional database for an enterprise e-commerce platform.

## Entity-Relationship Overview

```
customers ──< orders >── products
                │
                ▼
             payments

products ──< reviews >── customers
```

## Tables

### `customers`
| Column | Type | Description |
|--------|------|-------------|
| customer_id | UUID / INT (PK) | Unique customer identifier |
| name | VARCHAR | Customer full name |
| email | VARCHAR | Customer email (PII — mask in analytics contexts) |
| created_at | TIMESTAMP | Account creation time |

### `orders`
| Column | Type | Description |
|--------|------|-------------|
| order_id | UUID / INT (PK) | Unique order identifier |
| customer_id | FK → customers | Who placed the order |
| product_id | FK → products | What was ordered |
| quantity | INT | Units ordered |
| total_amount | DECIMAL | Order total |
| order_date | TIMESTAMP | When the order was placed |

### `products`
| Column | Type | Description |
|--------|------|-------------|
| product_id | UUID / INT (PK) | Unique product identifier |
| name | VARCHAR | Product name |
| category | VARCHAR | Product category |
| price | DECIMAL | Unit price |
| stock | INT | Units currently available |

### `payments`
| Column | Type | Description |
|--------|------|-------------|
| payment_id | UUID / INT (PK) | Unique payment identifier |
| order_id | FK → orders | Which order this payment covers |
| payment_method | VARCHAR | e.g., card, UPI, wallet |
| status | VARCHAR | pending / completed / failed / refunded |
| amount | DECIMAL | Amount charged |

### `reviews`
| Column | Type | Description |
|--------|------|-------------|
| review_id | UUID / INT (PK) | Unique review identifier |
| product_id | FK → products | What's being reviewed |
| customer_id | FK → customers | Who wrote the review |
| rating | INT (1–5) | Star rating |
| comment | TEXT | Free-text review body |

---

Besides this relational schema, two other data shapes flow through Generation and are sampled in this folder:
- **`clickstream_sample.json`** — semi-structured event data from the website/app (product views, add-to-cart, etc.)
- **`inventory_logs.csv`** — third-party warehouse stock-level feed

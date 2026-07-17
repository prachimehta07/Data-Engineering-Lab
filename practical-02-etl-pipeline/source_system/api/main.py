from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/transactions")
def get_transactions():
    with open("source_system/data/transactions.json", "r") as f:
        data = json.load(f)
    return data
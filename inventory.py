from fastapi import FastAPI
import random
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - INVENTORY - %(levelname)s - %(message)s')

@app.get("/check/{item_id}")
def check_inventory(item_id: int):
    in_stock = random.random() < 0.8 
    logging.info(f"Checked item {item_id}. In stock: {in_stock}")
    return {"item_id": item_id, "in_stock": in_stock}
from fastapi import FastAPI, HTTPException
import random
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - PAYMENT - %(levelname)s - %(message)s')

@app.post("/pay")
def process_payment(order: dict):
    if random.random() < 0.2:
        logging.error(f"Payment failed for order {order.get('id')}. Insufficient funds or timeout.")
        raise HTTPException(status_code=500, detail="Payment gateway error")
    
    logging.info(f"Successfully processed payment for order {order.get('id')} (Amount: ${order.get('amount')})")
    return {"status": "success", "transaction_id": random.randint(100000, 999999)}
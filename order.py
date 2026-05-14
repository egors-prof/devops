import time
import random
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - ORDER_APP - %(levelname)s - %(message)s')

INVENTORY_URL = "http://inventory:8000"
PAYMENT_URL = "http://payment:8000"

def simulate_traffic():
    logging.info("Starting traffic generator...")
    while True:
        order_id = random.randint(1000, 9999)
        item_id = random.randint(1, 50)
        amount = random.randint(10, 500)
        
        logging.info(f"--- New Order initiated: #{order_id} for item {item_id} ---")
        
        try:
            inv_res = requests.get(f"{INVENTORY_URL}/check/{item_id}")
            if inv_res.status_code == 200 and inv_res.json().get("in_stock"):
                pay_res = requests.post(f"{PAYMENT_URL}/pay", json={"id": order_id, "amount": amount})
                if pay_res.status_code == 200:
                    logging.info(f"Order #{order_id} completed successfully.")
                else:
                    logging.warning(f"Order #{order_id} failed at payment stage. Status: {pay_res.status_code}")
            else:
                logging.warning(f"Order #{order_id} cancelled. Item {item_id} is out of stock.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error while processing order #{order_id}: {e}")

        time.sleep(random.uniform(1, 4))

if __name__ == "__main__":
    simulate_traffic()
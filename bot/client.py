from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():
    client = Client(API_KEY, API_SECRET)

    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client

print("\nSUCCESS")
print("Order ID:", response.get("orderId"))
print("Status:", response.get("status"))
print("Executed Qty:", response.get("executedQty"))
print("Avg Price:", response.get("avgPrice", "N/A"))
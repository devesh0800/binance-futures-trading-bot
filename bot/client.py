from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():
    client = Client(
        api_key=API_KEY,
        api_secret=API_SECRET,
        testnet=True
    )

    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client

from bot.client import get_client

client = get_client()

try:
    account = client.futures_account()

    print("CONNECTED SUCCESSFULLY")
    print(account["totalWalletBalance"])

except Exception as e:
    print("ERROR:", e)
    
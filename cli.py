import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type
)

from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:

    side = validate_side(args.side)

    order_type = validate_order_type(args.type)

    if order_type == "LIMIT" and not args.price:
        raise ValueError(
            "Price required for LIMIT order"
        )

    client = get_client()

    response = place_order(
        client,
        args.symbol,
        side,
        order_type,
        args.quantity,
        args.price
    )

    print("\nSUCCESS")
    print("Order ID:", response["orderId"])
    print("Status:", response["status"])

except Exception as e:

    print("FAILED:", str(e))
    
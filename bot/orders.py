import logging

def place_order(client, symbol, side, order_type, quantity, price=None):

    try:

        logging.info(
            f"Order Request -> {symbol} {side} {order_type}"
        )

        if order_type == "MARKET":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        else:

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(response)

        return response

    except Exception as e:
        logging.error(str(e))
        raise
    
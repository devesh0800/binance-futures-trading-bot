# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot developed for Binance Futures Testnet (USDT-M). It allows users to place Market and Limit orders through a Command Line Interface (CLI) with proper validation, logging, and error handling.

## Features

* Place MARKET orders
* Place LIMIT orders
* Support BUY and SELL sides
* Command Line Interface (CLI)
* Input validation
* Structured logging
* Exception handling
* Binance Futures Testnet integration
* Environment variable support using `.env`

---

## Project Structure

```text
TradingBot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── .env
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/devesh0800/binance-futures-trading-bot.git

cd binance-futures-trading-bot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the root directory:

```env
API_KEY=YOUR_TESTNET_API_KEY
API_SECRET=YOUR_TESTNET_API_SECRET
```

> Note: Generate API credentials from Binance Futures Testnet, not Binance Mainnet.

---

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

## Input Parameters

| Parameter | Description                  |
| --------- | ---------------------------- |
| symbol    | Trading pair (e.g., BTCUSDT) |
| side      | BUY or SELL                  |
| type      | MARKET or LIMIT              |
| quantity  | Order quantity               |
| price     | Required for LIMIT orders    |

---

## Example Output

### Market Order

```text
SUCCESS

Order ID: 14549734339
Status: NEW
Executed Qty: 0.001
Avg Price: 0
```

### Limit Order

```text
SUCCESS

Order ID: 14549719183
Status: NEW
Executed Qty: 0
Avg Price: 0
```

---

## Logging

All API requests, responses, and errors are stored in:

```text
logs/trading.log
```

Example:

```text
2025-06-09 12:30:15 - INFO - Order Request -> BTCUSDT BUY MARKET
2025-06-09 12:30:16 - INFO - Order Response -> SUCCESS
```

---

## Error Handling

The application handles:

* Invalid order side
* Invalid order type
* Missing limit order price
* Binance API errors
* Network failures
* Invalid credentials

---

## Technologies Used

* Python 3.x
* python-binance
* python-dotenv
* argparse
* logging

---

## Assumptions

* User has a Binance Futures Testnet account.
* User has valid Testnet API credentials.
* Internet connection is available.

---

## Author

Devesh Duhan

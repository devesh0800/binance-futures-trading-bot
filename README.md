# Binance Futures Testnet Trading Bot

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- CLI based input
- Logging support
- Error handling
- Binance Futures Testnet integration

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create .env file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## Project Structure

```
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
├── cli.py
├── .env
├── requirements.txt
└── README.md
```

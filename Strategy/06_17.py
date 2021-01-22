import time
import pybithumb
import datetime

def get_target_price(ticker):
    df = pybithumb.get_candlestick(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

def buy_crypto_currency(ticker):
    krw = pybithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw/float(sell_price)
    pybithumb.buy_market_order(ticker, unit)

def sell_crypto_currency(ticker):
    unit = pybithumb.get_balance(ticker)[0]
    pybithumb.sell_market_order(ticker, unit)

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

target_price = get_target_price("BTC")

while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.delta(seconds=10):
        target_price = get_target_price("BTC")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
        sell_crypto_currency("BTC")

    current_price = pybithumb.get_current_price("BTC")
    if current_price > target_price:
        buy_crypto_currency("BTC")

    time.sleep(1)
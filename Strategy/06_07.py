import pybithumb
import time

con_key = "8dfb806e6f71213595690282985b5316"
sec_key = "de95da6be73e9a287ba1a86c21524611"

bithumb = pybithumb.Bithumb(con_key, sec_key)

krw = bithumb.get_balance("BTC")[2]
orderbook = pybithumb.get_orderbook("BTC")

asks = orderbook['asks']
sell_price = asks[0]['price']
unit = krw/float(sell_price)

order = bithumb.buy_market_order("BTC", unit)
print(order)
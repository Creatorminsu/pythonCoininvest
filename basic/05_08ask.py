import pybithumb

orderbook = pybithumb.get_orderbook("BTC")
asks = orderbook['asks']

for ask in asks:
    print(ask)
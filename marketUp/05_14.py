import pybithumb

btc = pybithumb.get_candlestick("BTC")
close = btc['close']
print(close)
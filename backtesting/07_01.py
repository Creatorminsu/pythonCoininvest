import pybithumb

df = pybithumb.get_candlestick("BTC")
print(df.tail())
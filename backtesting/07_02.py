import pybithumb

df = pybithumb.get_candlestick("BTC")
df.to_excel("btc.xlsx")
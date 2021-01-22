import pybithumb

df = pybithumb.get_candlestick("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df.to_excel("btc.xlsx")
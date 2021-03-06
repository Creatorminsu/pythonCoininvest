import pybithumb
import numpy as np

df = pybithumb.get_candlestick("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

df.to_excel("trade.xlsx")
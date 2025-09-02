import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf

style.use('ggplot')

##start = dt.datetime(2000,1,1)
##end= dt.datetime(2025,8,28)
##
##
##tsla = yf.Ticker('TSLA')
##df = tsla.history(start=start, end=end)
##
##df.to_csv('tsla.csv')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col = 0)

##print(df.head())

df['Close'].plot()
plt.show()
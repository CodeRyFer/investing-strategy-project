import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf

style.use('ggplot')

start = dt.datetime(2000,1,1)
end= dt.datetime(2025,8,28)

# Download Tesla stock data using yfinance
tsla = yf.Ticker('TSLA')
df = tsla.history(start=start, end=end)
print(df.head())
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col = 0)



df['Close'].plot()
plt.show()
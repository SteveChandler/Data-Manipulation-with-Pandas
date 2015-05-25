import pandas as pd
from pandas import DataFrame

import datetime
import pandas.io.data

import matplotlib.pyplot as plt


"""
sp500 = pd.io.data.get_data_yahoo('%5EGSPC',
                                  start = datetime.datetime(2000, 10, 1),
                                  end = datetime.datetime(2014, 6, 11))

sp500.to_csv('sp500_ohlc.csv')
"""

df = pd.read_csv('sp500_ohlc.csv', index_col='Date', parse_dates = True)
df['H-L'] = df['High'] - df.Low
df['100MA'] = pd.rolling_mean(df['Close'], 100, min_periods = 1)
df['Difference'] = df['Close'].diff()

df['STD'] = pd.rolling_std(df['Close'], 25, min_periods = 1)

print df.head()

ax1 = plt.subplot(2, 1, 1)
df['Close'].plot()

ax2 = plt.subplot(2, 1, 2, sharex = ax1)
df['STD'].plot()

plt.show()

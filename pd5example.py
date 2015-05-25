import pandas as pd
from pandas import DataFrame

import datetime
import pandas.io.data

import matplotlib.pyplot as plt

import random


"""
sp500 = pd.io.data.get_data_yahoo('%5EGSPC',
                                  start = datetime.datetime(2000, 10, 1),
                                  end = datetime.datetime(2014, 6, 11))

sp500.to_csv('sp500_ohlc.csv')
"""

df = pd.read_csv('sp500_ohlc.csv', index_col='Date', parse_dates = True)

def function(data):
    x = random.randrange(0,5)
    return data*x

df['Multiple'] = map(function, df['Close'])

print df.head()


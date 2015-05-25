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

print df[['Volume', 'H-L']].corr()

C = pd.io.data.get_data_yahoo('C',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
AAPL = pd.io.data.get_data_yahoo('AAPL',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
MSFT = pd.io.data.get_data_yahoo('MSFT',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
TSLA = pd.io.data.get_data_yahoo('TSLA',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
BAC = pd.io.data.get_data_yahoo('BAC',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
BBRY = pd.io.data.get_data_yahoo('BBRY',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
CMG = pd.io.data.get_data_yahoo('CMG',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
EBAY = pd.io.data.get_data_yahoo('EBAY',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
JPM = pd.io.data.get_data_yahoo('JPM',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
SBUX = pd.io.data.get_data_yahoo('SBUX',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
TGT = pd.io.data.get_data_yahoo('TGT',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
WFC = pd.io.data.get_data_yahoo('WFC',
                                 start=datetime.datetime(2011, 10, 1),
                                 end=datetime.datetime(2014, 1, 1))
print(C.head())
del C['Open']
del C['High']
del C['Low']
del C['Close']
del C['Volume']

corComp = C

corComp.rename(columns={'Adj Close': 'C'}, inplace=True)

corComp['BAC'] = BAC['Adj Close']
corComp['MSFT'] = MSFT['Adj Close']
corComp['TSLA'] = TSLA['Adj Close']

corComp['AAPL'] = AAPL['Adj Close']
corComp['BBRY'] = BBRY['Adj Close']
corComp['CMG'] = CMG['Adj Close']
corComp['EBAY'] = EBAY['Adj Close']
corComp['JPM'] = JPM['Adj Close']
corComp['SBUX'] = SBUX['Adj Close']
corComp['TGT'] = TGT['Adj Close']
corComp['WFC'] = WFC['Adj Close']

print(corComp.head())

print corComp.corr()
